import sys
from collections import deque
from copy import deepcopy

input()
input()
size = {}
used = {}
avail = {}
for line in sys.stdin:
    fn, sz, us, av, _ = line.split()
    x, y = map(lambda x: int(x[1:]), fn.split('-')[1:])
    if x not in size:
        size[x] = {}
        used[x] = {}
        avail[x] = {}
    size[x][y] = int(sz[:-1])
    used[x][y] = int(us[:-1])
    avail[x][y] = int(av[:-1])

viable = 0
for x1 in size:
    for y1 in size[x1]:
        for x2 in size:
            for y2 in size[x2]:
                if (x1, y1) != (x2, y2) and 0 < used[x1][y1] <= avail[x2][y2]:
                    viable += 1
print('Part 1:', viable)

goalx, goaly = max(used), min(used[max(used)])
update = 0
for x in used:
    for y in used[x]:
        if used[x][y] == 0:
            emptyx, emptyy = x, y
            update += 1

# Will also take a while
assert update == 1
q = deque([(goalx, goaly, emptyx, emptyy, 0, deepcopy(used))])
visited = {(goalx, goaly, emptyx, emptyy)}

curr_d = 0
while q:
    gx, gy, ex, ey, d, state = q.popleft()
    if curr_d != d:
        #print(d)
        curr_d = d
    if (gx, gy) == (0, 0):
        print('Part 2:', d)
        break
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        if ex + dx in size and ey + dy in size[ex + dx] and size[ex][ey] >= state[ex + dx][ey + dy] + state[ex][ey]:
            if (ex + dx, ey + dy) == (gx, gy):
                gx2, gy2 = ex, ey
            else:
                gx2, gy2 = gx, gy
            if (gx2, gy2, ex + dx, ey + dy) in visited:
                continue
            new_state = deepcopy(state)
            new_state[ex][ey] += new_state[ex + dx][ey + dy]
            new_state[ex + dx][ey + dy] = 0
            visited.add((gx2, gy2, ex + dx, ey + dy))
            q.append((gx2, gy2, ex + dx, ey + dy, d + 1, new_state))