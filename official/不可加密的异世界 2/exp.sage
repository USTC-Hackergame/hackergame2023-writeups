from pwn import remote, process
from itertools import product, combinations
from sage.modules.free_module_integer import IntegerLattice

io = remote("202.38.93.111",int(22000))
token = b"your token"
io.sendlineafter(b"token:", token)

# io = process(["sage","./chall.sage"])

p = 257 

# Directly taken from rbtree's LLL repository
# From https://oddcoder.com/LOL-34c3/, https://hackmd.io/@hakatashi/B1OM7HFVI
def Babai_CVP(mat, target):
    M = IntegerLattice(mat, lll_reduce=True).reduced_basis
    G = M.gram_schmidt()[0]
    diff = target
    for i in reversed(range(G.nrows())):
        diff -=  M[i] * ((diff * G[i]) / (G[i] * G[i])).round()
    return target - diff

def gen_oracle_list(n = 128):
    return [[ 0b10000000 if i==j else 0 for i in range(n)] for j in range(n)]

def bytes2vec(msg:bytes, base_ring):
    return vector(base_ring, [m for m in msg])

def enc_oracle(m):
    io.sendlineafter(b">", m.hex().encode())
    io.recvuntil(b"[+] you ciphertext : ")
    return bytes.fromhex(io.recvline().decode().strip())

def in_row_space(m, s):
    try:
        m.solve_left(s)
        return True
    except:
        return False
    
def xor(b1:bytes, b2:bytes):
    assert len(b1) == len(b2)
    return bytes([ i^^j for i,j in zip(b1,b2)])

def get_matrix_key(target_rank = 128):
    cnt = 0
    bs = []
    cs = []
    
    Zp = Zmod(257)
    basis = [vector(Zp, b) for b in gen_oracle_list()]
    for i in range(1,128):
        base = vector(Zp, [i]*128)
        cnt += 1
        base_ct = bytes2vec(enc_oracle(bytes(base)), Zp)
        if all(c!=0 for c in base_ct):
            break
    M = None
    num = 1
    
    while True:
        bf_space = combinations(basis, num)
        for btuple in bf_space:
            bv = sum(btuple)
            if M != None and in_row_space(M,bv):
                continue
            cv = bytes2vec(enc_oracle(bytes(bv + base)), Zp)
            cnt += 1
            if all(c!=0 for c in cv):
                bs.append(bv)
                cs.append(cv)
                M = matrix(Zp, bs)
                print(f"[+] query times = {cnt}, rank {len(bs)}")
                if M.rank() == target_rank:
                    B = matrix(Zp, bs).T
                    C = matrix(Zp, [ cv - base_ct for cv in cs]).T
                    # enc_matrix * B  = C
                    enc_matrix = C * B^(-1)
                    dec_matrix = enc_matrix^(-1)    
                    f1 = xor(bytes(vector(ZZ,dec_matrix*cs[0] - bs[0])% 256), bytes(base))
                    print("[+] flag1 :", f1)
                    print("[+] query times", cnt)
                    return enc_matrix, dec_matrix, f1
        num += 1
        
enc_matrix, dec_matrix, flag1 = get_matrix_key()
M = enc_matrix - 1
print(f"[+] {M.rank() = }")
M_rkernel = M.right_kernel_matrix()
Ip = identity_matrix(ZZ,M_rkernel.ncols())*p
M_rkernel_extended = block_matrix(ZZ, [M_rkernel, Ip], nrows = 2)

M_rkernel_reduced_p = M_rkernel_extended.BKZ(block_size = 20)

ascii_char_middle_value = (0x20 + 0x7f)//2
target_vector = vector(ZZ,[ascii_char_middle_value]*128)

vb = Babai_CVP(M_rkernel_reduced_p, target_vector)
print("[+] find payload : ", bytes(vb))
msg = bytes(vb)
io.sendlineafter(b">", msg.hex().encode())
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())