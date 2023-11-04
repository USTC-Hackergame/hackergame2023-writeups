import random
import math
from sympy import isprime

# You do know that we SCGY students can factor RSA, right?
# So just give me p and q directly
p = int(input('p: '))
q = int(input('q: '))
assert isprime(p) and isprime(q) and p != q

# Prove me that p, q are strong primes
lfp = int(input('A large prime factor of p-1: '))
lfq = int(input('A large prime factor of q-1: '))
assert isprime(lfp) and isprime(lfq)
assert (p-1) % lfp == 0 and (q-1) % lfq == 0
assert lfp > 2**128 and lfq > 2**128

N = p*q
phi = (p-1)*(q-1)
Nbits = N.bit_length()
# N is large enough
assert Nbits == 1024

e = int(input('e: ')) % phi
d = pow(e, -1, phi)
# No Low Private Exponent Attack
assert d.bit_length() > 0.292*Nbits
# No Low Public Exponent Attack
k = Nbits - max(int(Nbits*2/e), 96)

# OK, we've got a safe RSA parameters
state = random.SystemRandom().randint(2, N-1)
randomNums = []
states = []

mission = int(input("Choose mission: "))
if mission == 1:
    for _ in range(100):
        state = pow(state, e, N)
        randomNums.append(int(state) & ((1 << k) - 1))
        states.append(state)
elif mission == 2:
    for _ in range(1):
        state = state >> k
        state = pow(state, e, N)
        randomNums.append(int(state) & ((1 << k) - 1))
        states.append(state)

# Not a small loop
for i in range(len(states)-1):
    assert (math.gcd(states[i] - state, N) == 1)

print(randomNums)
guess = int(input("Predict PRNG state: "))
if guess == state:
    print(open(f"/flag{mission}").read())
