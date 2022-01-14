import sys

m = []
for line in sys.stdin:
    m.append(line.strip())

p, q = '', ''
for i in range(len(m[0])):
    d = {}
    for j in m:
        d[j[i]] = d.get(j[i], 0) + 1
    p += max(d, key=d.get)
    q += min(d, key=d.get)
print("Part 1:", p)
print("Part 2:", q)