cmds = input().strip().split(", ")
dir = 0
pos, found = [0, 0, 0, 0], []
v = set()
for i in range(len(cmds)):
    if cmds[i][0] == 'R':
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4
    for j in range(int(cmds[i][1:])):
        if (pos[0] - pos[2], pos[1] - pos[3]) not in v:
            v.add((pos[0] - pos[2], pos[1] - pos[3]))
        elif not found:
            found = pos.copy()
        pos[dir] += 1
print("Part 1:", abs(pos[0] - pos[2]) + abs(pos[1] - pos[3]))
print("Part 2:", abs(found[0] - found[2]) + abs(found[1] - found[3]))