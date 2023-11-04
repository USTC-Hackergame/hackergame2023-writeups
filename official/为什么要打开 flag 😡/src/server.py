# docker run arguments:
# "--tmpfs /dev/shm:exec" is required to run executable in /dev/shm
import subprocess
import base64
import os

STAGE = os.environ["STAGE"]
assert STAGE in ("1", "2")

if __name__ == "__main__":
    binary = input("Base64 of binary: ")
    with open("/dev/shm/executable", "wb") as f:
        f.write(base64.b64decode(binary))
    with open("/dev/shm/executable", "rb") as f:
        if f.read(4) != b"\x7fELF":
            print("不是 ELF 文件")
            exit(1)
    os.chmod("/dev/shm/executable", 0o555)
    if STAGE == "1":
        output = subprocess.run(
            ["/dev/shm/executable"],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            user="nobody",
            group="nogroup",
            env={
                "LD_PRELOAD": "/stage1.so"
            }
        )
    elif STAGE == "2":
        output = subprocess.run(
            ["/stage2", "/dev/shm/executable"],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            user="nobody",
            group="nogroup",
        )
    stdout = output.stdout[:8192].decode()
    stderr = output.stderr[:8192].decode()
    print("Return code:", output.returncode)
    print("stdout (标准输出，前 8192 个字节):")
    print(stdout)
    print("stderr (标准错误，前 8192 个字节):")
    print(stderr)
