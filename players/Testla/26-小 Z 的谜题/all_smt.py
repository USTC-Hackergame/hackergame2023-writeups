import itertools
import z3


bound = 5
constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3))
count = [3, 4, 2, 2, 2, 3]
num_constraints = sum(count)
num_dims = len(constraints[0])
arrange = [[[0 for i in range(3)] for j in range(num_dims)] for k in range(num_constraints)]

def all_smt(s, initial_terms):
    def block_term(s, m, t):
        s.add(t != m.eval(t, model_completion=True))
    def fix_term(s, m, t):
        s.add(t == m.eval(t, model_completion=True))
    def all_smt_rec(terms):
        if z3.sat == s.check():
            m = s.model()
            yield m
            for i in range(len(terms)):
                s.push()
                block_term(s, m, terms[i])
                for j in range(i):
                    fix_term(s, m, terms[j])
                yield from all_smt_rec(terms[i:])
                s.pop()
    yield from all_smt_rec(list(initial_terms))


solver = z3.Solver()
a = []
minus_1 = z3.Int('minus_1')
solver.add(minus_1 == 6)
index = 0
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

        index += 1

for m in all_smt(solver, [a[i][j][k] for i in range(num_constraints) for j in range(num_dims) for k in range(2)]):
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
    score = len(set((x, y, z) for i in range(num_constraints) for x, y, z in itertools.product(*l[i])))
    print(f'{score=}')
    l = sorted(l)
    for i in range(num_constraints):
        for j in range(num_dims):
            for k in range(2):
                print(l[i][j][k], end='')
    print()
