import itertools
import z3


bound = 5
constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3))
count = [3, 4, 2, 2, 2, 3]
num_constraints = sum(count)
num_dims = len(constraints[0])
arrange = [[[0 for i in range(3)] for j in range(num_dims)] for k in range(num_constraints)]

solver = z3.Solver()
a = []
minus_1 = z3.Int('minus_1')
solver.add(minus_1 == 6)
index = 0
s = z3.EmptySet(z3.IntSort())
for constraint, c in zip(constraints, count):
    for _ in range(c):
        element = [
            [
                z3.Int(f'a[{index}][{second_dim}][{0}]'),
                z3.Int(f'a[{index}][{second_dim}][{1}]'),
                minus_1,
            ]
            for second_dim in range(3)
        ]
        a.append(element)

        for second_dim in range(3):
            for k in range(2):
                solver.add(0 <= element[second_dim][k])
                solver.add(element[second_dim][k] <= 5)

        # stage 2
        for other_index in range(index):
            solver.add(z3.Or(*(
                z3.Or(
                    element[second_dim][1] <= a[other_index][second_dim][0],
                    a[other_index][second_dim][1] <= element[second_dim][0],
                )
                for second_dim in range(3)
            )))

        # stage 3
        solver.add(z3.Or(*(
            z3.And(*(
                element[second_dim][1] - element[second_dim][0] == diff[second_dim]
                for second_dim in range(3)
            ))
            for diff in set(itertools.permutations(constraint))
        )))

        # count cartesian product
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    s = z3.SetAdd(s, element[0][i] * 7 ** 2 + element[1][j] * 7 + element[2][k])

        index += 1

score = z3.Sum(*(
    z3.If(z3.IsMember(i * 7 ** 2 + j * 7 + k, s), 1, 0)
    for i in range(7)
    for j in range(7)
    for k in range(7)
))
solver.add(score >= 157)

check_result = solver.check()
print(check_result)
if check_result != z3.sat:
    exit(1)
m = solver.model()
l = [
    [
        [
            m[a[i][j][0]].as_long(),
            m[a[i][j][1]].as_long(),
            -1,
        ]
        for j in range(num_dims)
    ]
    for i in range(num_constraints)
]
print(f'{m[score]=}')
score = len(set((x, y, z) for i in range(num_constraints) for x, y, z in itertools.product(*l[i])))
print(f'{score=}')
l = sorted(l)
for i in range(num_constraints):
    for j in range(num_dims):
        for k in range(2):
            print(l[i][j][k], end='')
print()
