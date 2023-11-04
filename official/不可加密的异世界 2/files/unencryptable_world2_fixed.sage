from secrets import SystemRandom
import os
from string import printable
random = SystemRandom()

def random_square_matrix_with_fixed_rank(ring, nrows, rank):
    M = random_matrix(ring, rank, nrows)
    result = [list(row) for row in M]
    for i in range(nrows - rank):
        row = random_vector(ring, rank) * M
        result.append(row)
    random.shuffle(result)
    result_matrix = matrix(ring, result)
    assert M.rank() == rank, "bad matrix"
    return result_matrix

def random_square_matrix_with_full_rank(ring, nrows):
    result_matrix = random_square_matrix_with_fixed_rank(ring, nrows, nrows//2) + 1
    return result_matrix

def genearate_hill_key(n = 128, mod = 2**8 + 1):
    assert is_prime(mod), "only prime modulus"
    while True:
        M = random_square_matrix_with_full_rank(Zmod(mod), n)
        # equal to random_matrix(Zmod(mod), n) but returns a square matrix with full-rank and other features
        if M.rank() == n and gcd(M.det(),mod) == 1:
            return M

class hill_ciphersystem:
    base_mod = 2**8 + 1
    base_ring = GF(base_mod)
    key_len = None

    def __init__(self, key_matrix):
        assert key_matrix.is_square() and key_matrix.is_invertible(), "key must be square invertible matrix"
        self.encrypt_key = key_matrix
        self.decrypt_key = key_matrix**(-1)
        self.key_len = key_matrix.nrows()

    @classmethod
    def init(cls, key_len = 128):
        return cls(genearate_hill_key(key_len, cls.base_mod))

    @staticmethod
    def bytes2vec(msg:bytes, base_ring):
        return vector(base_ring, [m for m in msg])

    def encrypt(self, msg: bytes):
        # a buggy implementation, force 256 = 0
        assert len(msg) <= self.key_len
        msg = pad(msg, self.key_len)
        result = vector(ZZ,self.encrypt_key * self.bytes2vec(msg, self.base_ring)) % 256
        return bytes(result)

    def decrypt(self, ct: bytes):
        # a buggy implementation, your input \x00  might be 256 originally and then decrypted to another message
        assert len(ct) == self.key_len
        # ct = pad(ct, self.key_len)
        result = vector(ZZ,self.decrypt_key * self.bytes2vec(ct, self.base_ring)) % 256
        return bytes(result)

def xor(b1:bytes, b2:bytes):
    assert len(b1) == len(b2)
    return bytes([ i^^j for i,j in zip(b1,b2)])

def pad(msg:bytes, target_len):
    return msg + "".join([random.choice(printable) for _ in range(target_len - len(msg))]).encode()

class challenge:
    max_oracle_times = 400
    query_times = 0

    def __init__(self, xor_flag):
        self.hill_cipher = hill_ciphersystem.init()
        self.xor_flag = pad(xor_flag.encode(encoding = "ascii"), 128)

    def obfuscated_encrypt_oracle(self, msg: bytes):
        return self.hill_cipher.encrypt(xor(msg,self.xor_flag))

    def unencryptable_oracle(self, msg:bytes):
        return self.hill_cipher.encrypt(msg) == msg

    def oracle(self):
        print("[+] Welcome to hill cipher's magic world, the best hackers end up making it unencryptable!")
        print("[+] please give me some hex input (128 bytes) such as 77656c636f6d65 and I will check encrypt-ability for you.")
        while self.query_times < self.max_oracle_times:
            self.query_times += 1
            msg = bytes.fromhex(input(">"))
            assert len(msg) == 128, "bad input length"
            assert not all(m == 0 for m in msg), "zero vector forbidden"
            if self.unencryptable_oracle(msg):
                print("[+] unbelievable !!! You are an excellent hacker!")
                flag2 = open("/flag2", "r").read().strip()
                print(flag2)
                # check ascii
                if all( 0x20 <= m < 0x7f for m in msg):
                    print("[+] how can you find such an exquisite solution?")
                    flag3 = open("/flag3", "r").read().strip()
                    print(flag3)
            else:
                print("[+] In order not to reveal the key, I can only give you the obfuscated encrypted ciphertext.")
                print(f"[+] you ciphertext : {self.obfuscated_encrypt_oracle(msg).hex()}")
        print("[+] see you next time!")

if __name__ == "__main__":
    flag1 = open("/flag1", "r").read()
    challenge(flag1).oracle()