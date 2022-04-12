from hashlib import md5
from collections import deque
import sys

sys.setrecursionlimit(10**5)
SIZE = 4
passcode = input()

def BFS():
    p1 = False
    lp = 0
    q = deque([(0, '')])
    while q:
        xy, path = q.popleft()
        
        if xy == SIZE**2 - 1:
            if not p1:
                print('Part 1:', path)
                p1 = True
            lp = len(path)
            continue

        u, d, l, r = md5((passcode + path).encode('utf-8')).hexdigest()[:SIZE]
        if xy % SIZE > 0 and u in 'bcdef':
            q.append((xy - 1, path + 'U'))
        if xy // SIZE > 0 and l in 'bcdef':
            q.append((xy - SIZE, path + 'L'))
        if xy % SIZE < SIZE - 1 and d in 'bcdef':
            q.append((xy + 1, path + 'D'))
        if xy // SIZE < SIZE - 1 and r in 'bcdef':
            q.append((xy + SIZE, path + 'R'))
    print('Part 2:', lp)

def DFS():
    lp = [0]

    def trav(xy, path):
        if xy == SIZE**2 - 1:
            lp[0] = max(lp[0], len(path))
            return
        u, d, l, r = md5((passcode + path).encode('utf-8')).hexdigest()[:SIZE]
        if xy % SIZE > 0 and u in 'bcdef':
            trav(xy - 1, path + 'U')
        if xy // SIZE > 0 and l in 'bcdef':
            trav(xy - SIZE, path + 'L')
        if xy % SIZE < SIZE - 1 and d in 'bcdef':
            trav(xy + 1, path + 'D')
        if xy // SIZE < SIZE - 1 and r in 'bcdef':
            trav(xy + SIZE, path + 'R')

    trav(0, '')
    print('Part 2 (DFS):', lp[0])

BFS()
DFS()