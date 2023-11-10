import sys
import json
import random
import itertools
import subprocess

import numpy as np
from tqdm import tqdm
from pwn import remote


def arr_add(a, b, base=2**8+1):
    return [(x+y) % base for x, y in zip(a, b)]


def arr_sub(a, b, base=2**8+1):
    return [(x-y) % base for x, y in zip(a, b)]


def matrix_modular_inverse(mat):
    js = subprocess.run(
        ["node", "js/mat_mod_inv.js"],
        input = json.dumps(mat.tolist()).encode() + b"\n",
        stdout = subprocess.PIPE,
        check = True,
    )
    print("js.stdout = ", end="")
    if len(js.stdout) <= 103:
        print(js.stdout)
    else:
        print(js.stdout[:50] + b"..." + js.stdout[-50:])

    return np.array(json.loads(js.stdout), dtype=np.uint32)


def main():
    conn = remote("202.38.93.111", 22000)
    conn.interactive()

    basearr = bytearray(128)
    basearr[:4] = b"flag"

    conn.send(basearr.hex().encode() + b"\n")
    conn.recvuntil(b"you ciphertext : ")
    basearr_encrypted = bytes.fromhex(conn.recvline().decode())
    assert 0 not in basearr_encrypted
    print(f"{basearr_encrypted.hex() = }")

    # 如果遇到输出中的零，就再改变输入中的几位，重试
    # 把已知为 0 的一些位改为 1
    # >>> [f"{c} {ord(c):08b}" for c in "flag"]
    # ['f 01100110',
    #  'l 01101100',
    #  'a 01100001',
    #  'g 01100111']
    single_solutions = [
        (0, 2**0), (0, 2**3), (0, 2**4),
        (1, 2**0), (1, 2**1), (1, 2**4),
        (2, 2**1), (2, 2**2), (2, 2**3), (2, 2**4),
        (3, 2**3), (3, 2**4),
    ]
    solutions = [
        [(0, 0)],  # NOP
        *[[s] for s in single_solutions],
        *itertools.combinations(single_solutions, 2),
        *itertools.combinations(single_solutions, 3),
        *itertools.combinations(single_solutions, 4),
        *itertools.combinations(single_solutions, 5),
        *itertools.combinations(single_solutions, 6),
    ]

    # 获取一系列明文-密文对
    plaintexts = []
    ciphertexts = []
    progress_bar = iter(tqdm(range(400)))
    next(progress_bar)

    for i in range(128):
        for solution in solutions:
            # Key @ (arr_a + arr_b) == Key @ arr_a + Key @ arr_b
            arr = [0] * 128
            arr[i] += 2**7
            for ind, value in solution:
                arr[ind] += value

            next(progress_bar)
            conn.recvuntil(b">")
            conn.send(bytes(arr_add(basearr, arr)).hex().encode() + b"\n")
            conn.recvuntil(b"you ciphertext : ")
            encrypted = bytes.fromhex(conn.recvline().decode())

            if 0 not in encrypted:
                break
        else:
            progress_bar.close()
            print("all solutions are used up. give up.")
            sys.exit(1)

        plaintexts.append(arr)
        ciphertexts.append(arr_sub(encrypted, basearr_encrypted))

    progress_bar.close()

    # 根据明文-密文对来计算加密矩阵，也即密钥
    # Key @ Plain == Cipher
    # Key @ Plain @ Plain^-1 == Cipher @ Plain^-1

    plain_matrix = np.array(plaintexts, dtype=np.uint32).T
    cipher_matrix = np.array(ciphertexts, dtype=np.uint32).T

    base = 2**8 + 1
    plain_matrix_inv = matrix_modular_inverse(plain_matrix)
    key_matrix = (cipher_matrix @ plain_matrix_inv) % base
    print("key_matrix = ")
    print(key_matrix)

    for i, (plain, cipher) in enumerate(zip(plaintexts, ciphertexts)):
        plain_array = np.array(plain, dtype=np.uint32)
        cipher_expect = list(cipher)
        cipher_computed = list((key_matrix @ plain_array) % base)
        if cipher_expect != cipher_computed:
            print(f"{i = }")
            print(f"{cipher_computed = }")
            print(f"{cipher_expect = }")
            raise AssertionError

    print("key verified.")

    decrypt_key_matrix = matrix_modular_inverse(key_matrix)
    print("decrypt_key_matrix = ")
    print(decrypt_key_matrix)

    flag_arr = decrypt_key_matrix @ np.array(list(basearr_encrypted), dtype=np.uint32) % base
    print("flag =", bytes(list(flag_arr % (2**8))))


main()
