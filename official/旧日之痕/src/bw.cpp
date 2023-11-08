#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Support/raw_ostream.h"

#include <cstdint>
#include <iostream>
#include <random>

using namespace llvm;

static cl::opt<std::string>
    WatermarkStr("watermark-str", cl::init(""),
                 cl::desc("Specify string to be used as watermark"),
                 cl::value_desc("str"));

namespace {

static const uint8_t cantor_bitlen[] = {
    0,  0,  1,  2,  4,  6,  9,  12, 15, 18, 21, 25,  28,  32,  36,  40,  44, 48,
    52, 56, 61, 65, 69, 74, 79, 83, 88, 93, 97, 102, 107, 112, 117, 122, 127};

static const uint8_t b64idx[256] = {
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 57,  20,  255, 4,   11,  45,  38,  43,  56,  39,  255, 255,
    255, 255, 255, 255, 255, 6,   36,  41,  63,  12,  21,  58,  10,  40,  33,
    59,  54,  15,  3,   31,  5,   47,  25,  61,  2,   26,  34,  9,   53,  18,
    1,   255, 255, 255, 255, 29,  255, 55,  0,   50,  8,   46,  17,  19,  35,
    7,   62,  52,  16,  60,  32,  44,  13,  22,  42,  51,  37,  30,  24,  48,
    23,  14,  27,  49,  255, 28,  255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255};

void encode(Function &F, __int128_t cantor) {
  //assert(cantor >= 0);

  std::vector<BasicBlock *> allBB;
  for (BasicBlock &tmp : F) {
    if (tmp.size() != 1)
      allBB.push_back(&tmp);
  }

  uint8_t fsize =
      allBB.size() > sizeof(cantor_bitlen) ? sizeof(cantor_bitlen) : allBB.size();
  std::vector<uint8_t> expansion(fsize, 0), index(fsize, 0), validi(fsize - 1);
  std::iota(validi.begin(), validi.end(), 1);
  int i = 1;
  while (cantor != 0) {
    //assert(i < fsize - 1);
    expansion[i] = cantor % (i + 1);
    cantor = (cantor - expansion[i]) / (i + 1);
    i++;
  }
  for (i = 1; i < fsize; i++) {
    index[i] = validi[expansion[fsize - i - 1]];
    validi.erase(validi.begin() + expansion[fsize - i - 1]);
  }

  for (i = 1; i < fsize; i++) {
    allBB[index[i]]->moveAfter(allBB[index[i - 1]]);
  }

  F.addFnAttr(Attribute::NoInline);
  F.addFnAttr(Attribute::OptimizeNone);
}

std::vector<bool> constructBW(std::string str) {
  std::vector<uint8_t> ubw;
  std::vector<bool> bw;
  ubw.push_back(str.length());
  for (int c : str) {
    if (c < 0 || c > 255 || b64idx[c] == 255) {
      return bw;
    }
    ubw.push_back(b64idx[c]);
  }
  uint8_t parity = 0;
  for (uint8_t i : ubw) {
    //assert(i < 64);
    parity ^= (i) ^ (i >> 1) ^ (i >> 2) ^ (i >> 3) ^ (i >> 4) ^ (i >> 5);
    bw.push_back((i >> 5) & 1);
    bw.push_back((i >> 4) & 1);
    bw.push_back((i >> 3) & 1);
    bw.push_back((i >> 2) & 1);
    bw.push_back((i >> 1) & 1);
    bw.push_back(i & 1);
  }
  parity &= 1;
  bw[0] = parity;
  std::mt19937 g(ubw[0] + (parity << 5));
  std::shuffle(bw.begin() + 6, bw.end(), g);
  return bw;
}

// New PM implementation
struct BinaryWatermark : PassInfoMixin<BinaryWatermark> {
  // Main entry point, takes IR unit to run the pass on (&F) and the
  // corresponding pass manager (to be queried if need be)
  PreservedAnalyses run(Module &M, ModuleAnalysisManager &) {
    if (WatermarkStr == "") {
      errs() << "Please specify watermark string!\n";
      return PreservedAnalyses::all();
    }
    if (WatermarkStr.length() >= 32) {
      errs() << "Watermark too long!\n";
      return PreservedAnalyses::all();
    }
    auto bw = constructBW(WatermarkStr);
    if (bw.size() == 0) {
      errs() << "Invalid watermark string!\n";
      return PreservedAnalyses::all();
    }
    uint32_t capacity = 0;
    std::vector<Function *> functions;
    for (Function &F : M) {
      if (F.getName().starts_with("llvm")) {
        continue;
      }
      uint8_t fsize = std::count_if(F.begin(), F.end(), [](BasicBlock &BB) {
        return BB.size() > 1;
      });
      fsize = fsize > sizeof(cantor_bitlen) ? sizeof(cantor_bitlen) : fsize;
      if (fsize > 3) {
        capacity += cantor_bitlen[fsize - 1];
        functions.push_back(&F);
      }
      if (capacity >= bw.size()) {
        break;
      }
    }
    if (capacity < bw.size()) {
      errs() << "Watermark too long!\n";
      return PreservedAnalyses::all();
    }
    uint8_t counter = 0;
    for (Function *F : functions) {
      uint8_t fsize = std::count_if(F->begin(), F->end(), [](BasicBlock &BB) {
        return BB.size() > 1;
      });
      fsize = fsize > sizeof(cantor_bitlen) ? sizeof(cantor_bitlen) : fsize;
      uint8_t cbitlen = cantor_bitlen[fsize - 1];
      cbitlen = counter + cbitlen > bw.size() ? bw.size() - counter : cbitlen;
      __int128_t cantor = 0;
      for (auto it = bw.begin() + counter; it != bw.begin() + counter + cbitlen;
           ++it) {
        cantor <<= 1;
        cantor += *it;
      }
      encode(*F, cantor);
      counter += cbitlen;
    }
    return PreservedAnalyses::none();
  }

  // Without isRequired returning true, this pass will be skipped for functions
  // decorated with the optnone LLVM attribute. Note that clang -O0 decorates
  // all functions with optnone.
  static bool isRequired() { return true; }
};
} // namespace

//-----------------------------------------------------------------------------
// New PM Registration
//-----------------------------------------------------------------------------
llvm::PassPluginLibraryInfo getBinaryWatermarkPluginInfo() {
  return {LLVM_PLUGIN_API_VERSION, "BinaryWatermark", LLVM_VERSION_STRING,
          [](PassBuilder &PB) {
            PB.registerPipelineParsingCallback(
                [](StringRef Name, ModulePassManager &MPM,
                   ArrayRef<PassBuilder::PipelineElement>) {
                  if (Name == "binary-watermark") {
                    MPM.addPass(BinaryWatermark());
                    return true;
                  }
                  return false;
                });
          }};
}

// This is the core interface for pass plugins. It guarantees that 'opt' will
// be able to recognize BinaryWatermark when added to the pass pipeline on the
// command line, i.e. via '-passes=binary-watermark'
extern "C" LLVM_ATTRIBUTE_WEAK ::llvm::PassPluginLibraryInfo
llvmGetPassPluginInfo() {
  return getBinaryWatermarkPluginInfo();
}
