import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def bezout(a, b):
    if a == 0:
        return 0, 1
    elif b == 0:
        return 1, 0
    else:
        p, q = bezout(b, a % b)
        return (q, p - q * (a // b))

congs = []
for line in sys.stdin:
    line = line.split()
    a, m = int(line[-1][:-1]), int(line[3])
    congs.append(((m - a - len(congs) - 1) % m, m))

a, m = congs[0]
for b, n in congs[1:]:
    d = gcd(m, n)
    k = m * n // d
    u, _ = bezout(m, n)
    a, m = (a - m * u * (a - b) // d) % k, k
print('Part 1:', a)

# One more CRT iteration
aa, mm = 0, 11
b, n = (mm - aa - len(congs) - 1) % mm, mm
d = gcd(m, n)
k = m * n // d
u, _ = bezout(m, n)
print('Part 2:', (a - m * u * (a - b) // d) % k)