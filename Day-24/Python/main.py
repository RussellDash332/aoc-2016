import sys
from heapq import *
from collections import deque

NODES = 8

m = []
for line in sys.stdin:
    m.append(list(line.strip()))

r, c = len(m), len(m[0])
node = [None] * NODES
for i in range(r):
    for j in range(c):
        if m[i][j] in map(str, range(NODES)):
            node[int(m[i][j])] = c*i + j

D = {}
for n in range(NODES):
    source = node[n]
    D[n] = [float('inf')] * (r*c)
    q = deque([(source, 0)])
    D[n][source] = 0
    visited = {source}
    while q:
        u, d = q.popleft()
        ur, uc = u // c, u % c
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= ur + dr < r and 0 <= uc + dc < c and c*(ur + dr) + uc + dc not in visited and m[ur + dr][uc + dc] != '#':
                visited.add(c*(ur + dr) + uc + dc)
                D[n][c*(ur + dr) + uc + dc] = d + 1
                q.append((c*(ur + dr) + uc + dc, d + 1))
    temp = {}
    for i in range(NODES):
        if i != n:
            temp[i] = D[n][node[i]]
    D[n] = temp
g = D

g2 = {}
for u in g:
    for v in g[u]:
        for _ in range(2):
            for i in range(2**NODES):
                if 2**NODES*u + i not in g2:
                    g2[2**NODES*u + i] = {}
                g2[2**NODES*u + i][2**NODES*v + i|2**v] = g[u][v]
            u, v = v, u

D = [float('inf')] * (2**NODES * NODES)
D[0] = 0
pq = [(0, 0)]

while pq:
    dd, vv = heappop(pq)
    if dd == D[vv] and vv in g2:
        for nn in g2[vv]:
            if D[nn] > dd + g2[vv][nn]:
                D[nn] = dd + g2[vv][nn]
                heappush(pq, (D[nn], nn))
print('Part 1:', min(D[2**NODES - 2::2**NODES]))
print('Part 2:', D[2**NODES - 1])