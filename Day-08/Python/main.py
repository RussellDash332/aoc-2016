import sys

m = []
W, H = 50, 6

for _ in range(H):
    m.append([0] * W)

for line in sys.stdin:
    cmd = line.strip().split()
    if cmd[0] == 'rect':
        c, r = cmd[1].split('x')
        c, r = int(c), int(r)
        for i in range(r):
            for j in range(c):
                m[i][j] = 1
    elif cmd[1] == 'column':
        pos = int(cmd[2][2:])
        dis = int(cmd[-1])
        tmp = list(map(lambda x: x[pos], m))
        for _ in range(dis):
            tmp.insert(0, tmp.pop())
        for i in range(H):
            m[i][pos] = tmp[i]
    else:
        pos = int(cmd[2][2:])
        dis = int(cmd[-1])
        tmp = m[pos]
        for _ in range(dis):
            tmp.insert(0, tmp.pop())
        for i in range(H):
            m[pos][i] = tmp[i]
print("Part 1:", sum(map(sum, m)))
print("Part 2:")
for row in m:
    print(''.join(list(map(lambda x: [' ', '*'][x], row))))