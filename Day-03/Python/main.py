import sys

possible = 0
m = []
for line in sys.stdin:
    a, b, c = list(map(int, line.strip().split()))
    possible += int(a + b + c > 2 * max(a, b, c))
    m.append([a, b, c])
print("Part 1:", possible)

possible2 = 0
for i in range(0, len(m), 3):
    for j in range(3):
        possible2 += int(m[i][j] + m[i + 1][j] + m[i + 2][j] > 2 * max(m[i][j], m[i + 1][j], m[i + 2][j]))
print("Part 2:", possible2)