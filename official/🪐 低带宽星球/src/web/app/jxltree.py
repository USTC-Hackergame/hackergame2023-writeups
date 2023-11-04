import random

TEMPLATE = """RCT 0
if x > {x1}
  if c > 1
    - Set {set1b}
    if c > 0
      - Set {set1g}
      - Set {set1r}
  if x > {x2}
    if c > 1
      - Set {set2b}
      if c > 0
        - Set {set2g}
        - Set {set2r}
    if c > 1
      - Set {set3b}
      if c > 0
        - Set {set3g}
        - Set {set3r}
"""

def generate_res(seed: str, cost: int = 0) -> str:
    r = random.Random(seed)
    for _ in range(cost):
        r.randint(0, 1000)
    x1 = r.randint(650, 750)
    x2 = r.randint(300, 400)
    # while x2 == x1:
    #     x2 = r.randint(0, 1000)
    # if x1 < x2:
    #     x1, x2 = x2, x1
    bs = []; gs = []; rs = []
    set1b = r.randint(0, 255); bs.append(set1b)
    set1g = r.randint(0, 255); gs.append(set1g)
    set1r = r.randint(0, 255); rs.append(set1r)

    set2b = r.randint(0, 255)
    while set2b in bs:
        set2b = r.randint(0, 255)
    bs.append(set2b)

    set2g = r.randint(0, 255)
    while set2g in gs:
        set2g = r.randint(0, 255)
    gs.append(set2g)

    set2r = r.randint(0, 255)
    while set2r in rs:
        set2r = r.randint(0, 255)
    rs.append(set2r)

    set3b = r.randint(0, 255)
    while set3b in bs:
        set3b = r.randint(0, 255)
    # bs.append(set3b)

    set3g = r.randint(0, 255)
    while set3g in gs:
        set3g = r.randint(0, 255)
    # gs.append(set3g)

    set3r = r.randint(0, 255)
    while set3r in rs:
        set3r = r.randint(0, 255)
    # rs.append(set3r)

    return TEMPLATE.format(
        x1=x1,
        x2=x2,
        set1b=set1b,
        set1g=set1g,
        set1r=set1r,
        set2b=set2b,
        set2g=set2g,
        set2r=set2r,
        set3b=set3b,
        set3g=set3g,
        set3r=set3r,
    )
