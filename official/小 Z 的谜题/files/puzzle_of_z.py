import itertools


bound = 5
constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3))
count = [3, 4, 2, 2, 2, 3]
num_constraints = sum(count)
num_dims = len(constraints[0])
arrange = [[[0 for i in range(3)] for j in range(num_dims)] for k in range(num_constraints)]
print('Input a string:')
s = (c for c in input().strip())
for i in range(num_constraints):
    for j in range(num_dims):
        for k in range(3):
            if k == 2:
                arrange[i][j][k] = -1
            else:
                number = int(next(s))
                assert 0 <= number <= bound
                arrange[i][j][k] = number
print('Stage 0 passed')
assert arrange == list(sorted(arrange))
print('Stage 1 passed')
for i in range(num_constraints):
    for j in range(num_constraints):
        if i == j:
            continue
        assert any((arrange[i][k][1] <= arrange[j][k][0] or arrange[j][k][1] <= arrange[i][k][0]) for k in range(num_dims))
print('Stage 2 passed')
for i in range(num_constraints):
    for t in range(len(constraints)):
        if tuple(sorted([arrange[i][j][1] - arrange[i][j][0] for j in range(num_dims)])) == constraints[t]:
            count[t] -= 1
            break
assert not any(count)
print('Stage 3 passed')
score = len(set((x, y, z) for i in range(num_constraints) for x, y, z in itertools.product(*arrange[i])))
if score >= 157:
    print(open('/flag3').read())
elif score <= 136:
    print(open('/flag2').read())
else:
    print(open('/flag1').read())
