# This script is NOT used in the final product. It was used to generate some
# images to check if the algorithm was working correctly.

from jxltree import generate_res
import subprocess
# import os

dir = "./images/"

for token_id in range(1024):
    print(token_id)
    cost = 0
    while True:
        tree = generate_res(token_id, cost)
        r1 = subprocess.run(
            ["jxl_from_tree", "/dev/stdin", "/dev/stdout"],
            input=tree.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if r1.returncode != 0:
            print(r1.stderr.decode())
            raise RuntimeError("Failed to generate. Please contact admin.", 500)
        jxl_bytes = r1.stdout
        if len(jxl_bytes) > 50:
            print("size > 50, retry")
            cost += 1
        else:
            break
    # write jxl to file, as djxl fails to read from stdin
    with open(f"{dir}/{token_id}.jxl", "wb") as f:
        f.write(jxl_bytes)
    r2 = subprocess.run(
        ["djxl", f"{dir}/{token_id}.jxl", f"{dir}/{token_id}.png"],
        input=jxl_bytes,
        stderr=subprocess.PIPE,
    )
    # os.remove(f"{dir}/{token_id}.jxl")
    if r2.returncode != 0:
        print(r2.stderr.decode())
        raise RuntimeError("Failed to generate. Please contact admin.", 500)