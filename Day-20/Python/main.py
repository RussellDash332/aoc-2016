import sys

rng = []
for line in sys.stdin:
    a, b = map(int, line.split('-'))
    rng.append((a, b))
rng.sort()
seq = [(-1, -1)]
for a, b in rng:
    s, e = seq[-1]
    if a <= s <= b + 1 or s <= a <= e + 1:
        seq.pop()
        seq.append((max(0, min(a, s)), max(b, e)))
    else:
        seq.append((a, b))
print('Part 1:', seq[0][1] + 1)

allow = 0
for i in range(1, len(seq)):
    allow += seq[i][0] - seq[i - 1][1] - 1
allow += 2**32 - 1 - seq[-1][-1]
print('Part 2:', allow)