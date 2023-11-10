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
a = [
    [
        [
            z3.Int(f'a[{index}][{second_dim}][{k}]')
            for k in range(2)
        ]
        for second_dim in range(3)
    ]
    for index in range(num_constraints)
]
all_terms = [a[i][j][k] for i in range(num_constraints) for j in range(num_dims) for k in range(2)]

def process_model(m):
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

for index in range(num_constraints):
    element = a[index]

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

unique_diff_combs = []
for i in range(len(constraints)):
    unique_diffs = set(itertools.permutations(constraints[i]))
    unique_diff_combs.append(set(map(tuple, map(sorted, itertools.product(*itertools.repeat(unique_diffs, count[i]))))))
# print(list(len(c) for c in unique_diff_combs))
# 10 * 15 * 21 * 6 * 10
# 189000

leave_count = 0
def search(ci: int):
    global leave_count

    for diff_comb in unique_diff_combs[ci]:
        solver.push()

        # stage 3
        for offset in range(count[ci]):
            diff = diff_comb[offset]
            element = a[sum(count[:ci]) + offset]
            for second_dim in range(3):
                solver.add(element[second_dim][1] - element[second_dim][0] == diff[second_dim])
                # Should we limit the range here?
                # solver.add(element[second_dim][1] >= diff[second_dim])
                # solver.add(element[second_dim][0] <= 5 - diff[second_dim])
                # No, to reach leave 12, 16s without extra info, 22s with.
                # solver.add(element[second_dim][1] >= diff[second_dim])
                # solver.add(element[second_dim][1] <= 5)
                # solver.add(element[second_dim][0] <= 5 - diff[second_dim])
                # solver.add(element[second_dim][0] >= 0)
                # Moving the basic requirement here doesn't help, either.

        if ci == len(count) - 1:
            leave_count += 1
            print(f'{leave_count=}')
            for m in all_smt(solver, all_terms):
                process_model(m)
        else:
            search(ci + 1)

        solver.pop()

search(0)
