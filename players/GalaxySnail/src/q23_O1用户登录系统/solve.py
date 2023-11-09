import sys
from hashlib import sha1
from pwn import *

#                     -------------------
#                     | root (hash_a_b) |
#                     -------------------
#                              |
#             ------------------------------------
#             |     hash_a     |      hash_b     |
#             ------------------------------------
#      user_a       /                     \         user_b
# ----------------------            ------------------------------
# |  hash_1  |  hash_2 |            |  hash_admin  |   hash_3    |
# ----------------------            ------------------------------
#     /           \                      /                \
# -----------  -----------        ---------------     --------------
# |  1:??   |  |  2:??   |        |  admin:??   |     |    3:??    |
# -----------  -----------        ---------------     --------------

def assert_eq(a, b):
    if a != b:
        print(f"assert left : {a!r}")
        print(f"assert right: {b!r}")
        raise AssertionError

def validate_hash(digest, part="left"):
    assert digest.isascii()
    if part == "left":
        assert b":" in digest
        assert digest[0] < 64
        assert digest.lstrip() == digest
    elif part == "right":
        assert b":" not in digest
        assert digest[0] >= 64
        assert digest.rstrip() == digest
    else:
        assert False

def main():
    # prepare hash
    user_1 = b"1:43024421"
    hash_1 = sha1(user_1).digest()
    validate_hash(hash_1)

    user_2 = b"2:7795620"
    hash_2 = sha1(user_2).digest()
    validate_hash(hash_2, "right")

    admin = b"admin:1690553"
    hash_admin = sha1(admin).digest()
    validate_hash(hash_admin)

    user_3 = b"3:3543994"
    hash_3 = sha1(user_3).digest()
    validate_hash(hash_3, "right")

    user_a = hash_1 + hash_2
    hash_a = sha1(user_a).digest()
    user_b = hash_admin + hash_3
    hash_b = sha1(user_b).digest()

    # start
    conn = remote("202.38.93.111", 10094)
    conn.interactive()

    conn.send(b"1\n")
    conn.recvuntil(b"> ")
    conn.send(user_a + b"\n")
    conn.recvuntil(b"> ")
    conn.send(user_b + b"\n")
    conn.recvuntil(b"> ")
    conn.send(b"EOF\n")

    conn.recvuntil(b"Login credentials:\n")
    cred_a = conn.recvline().rstrip()
    cred_b = conn.recvline().rstrip()

    print(f"{hash_a.hex() = }")
    print(f"{hash_b.hex() = }")
    print(f"{cred_a = }")
    print(f"{cred_b = }")

    assert_eq(cred_a.rsplit(b":")[-1].decode(), hash_b.hex())
    assert_eq(cred_b.rsplit(b":")[-1].decode(), hash_a.hex())

    conn.interactive()
    conn.send(b"2\n")
    conn.recvuntil(b"Login credential: ")
    admin_cred = admin + b":" + hash_3.hex().encode() + hash_a.hex().encode()
    print(admin_cred)
    conn.send(admin_cred + b"\n")

    conn.interactive()

main()
