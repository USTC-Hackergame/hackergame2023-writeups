from hashlib import sha1
from tqdm import tqdm

def find_hash(prefix, part="left", start=0):
    for i in tqdm(iter(range(start, 2**32))):
        orig = prefix + b"%d" % i
        digest = sha1(orig).digest()

        if not digest.isascii():
            continue

        if part == "left":
            if b":" not in digest or digest[0] >= 64 or digest.lstrip() != digest:
                continue
        elif part == "right":
            if b":" in digest or digest[0] < 64 or digest.rstrip() != digest:
                continue
        else:
            assert False

        tqdm.write(f"{orig = }, sha1 = {digest}, {digest[0] = }")
        break

def main():
    print("user 1")
    find_hash(b"1:")
    print()
    print("user 2")
    find_hash(b"2:", "right")
    print()
    print("user admin")
    find_hash(b"admin:")
    print()
    print("user 3")
    find_hash(b"3:", "right")

main()
