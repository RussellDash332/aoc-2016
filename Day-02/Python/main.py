import sys

s, t = "", ""
d = {
    (0, 2): 1,
    (1, 1): 2,
    (1, 2): 3,
    (1, 3): 4,
    (2, 0): 5,
    (2, 1): 6,
    (2, 2): 7,
    (2, 3): 8,
    (2, 4): 9,
    (3, 1): 'A',
    (3, 2): 'B',
    (3, 3): 'C',
    (4, 2): 'D'
}
for line in sys.stdin:
    r1, c1, r2, c2 = 1, 1, 2, 0
    for m in line.strip():
        if m == 'U':
            r1 = max(0, r1 - 1)
            if r2 != abs(c2 - 2):
                r2 -= 1
        elif m == 'D':
            r1 = min(2, r1 + 1)
            if r2 != 4 - abs(c2 - 2):
                r2 += 1
        elif m == 'L':
            c1 = max(0, c1 - 1)
            if c2 != abs(r2 - 2):
                c2 -= 1
        else:
            c1 = min(2, c1 + 1)
            if c2 != 4 - abs(r2 - 2):
                c2 += 1
    s += str(3 * r1 + c1 + 1)
    t += str(d[(r2, c2)])
print("Part 1:", s)
print("Part 2:", t)