fav = int(input())

def f(x, y):
    return x*x + 3*x + 2*x*y + y + y*y + fav

def g(x, y):
    return ['.', '#'][sum(map(int, bin(f(x, y))[2:])) % 2]

m, size = [], 100
for y in range(size):
    temp = []
    for x in range(size):
        temp.append(g(x, y))
    m.append(temp)

graph = {}
for x in range(size):
    for y in range(size):
        graph[(x, y)] = set()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if m[y][x] != '#' and abs(dx) + abs(dy) == 1 and 0 <= x + dx < size and 0 <= y + dy < size:
                    if m[y + dy][x + dx] != '#':
                        graph[(x, y)].add((x + dx, y + dy))

def BFS(graph):
    par = {}
    depth = {(1, 1): 0}
    q = [(1, 1, 0)]
    while q:
        x, y, d = q.pop(0)
        if (x, y) in graph:
            for suc in graph[(x, y)]:
                if suc not in depth:
                    q.append((*suc, d + 1))
                    depth[suc] = d + 1
                    par[suc] = (x, y)
    return depth

k = BFS(graph)
print('Part 1:', k[(31, 39)])
print('Part 2:', sum(map(lambda x: int(x <= 50), k.values())))