import sys, string
from copy import deepcopy

letters = string.ascii_lowercase

cmd = []
for line in sys.stdin:
    cmd.append(line.strip().split())

def simulate(aval, cmd):
    reg, pos = {}, 0
    for k in 'abcd':
        reg[k] = 0
    reg['a'] = aval
    while pos < len(cmd):
        c = cmd[pos]
        if c[0] == 'cpy':
            if c[1] in reg:
                reg[c[2]] = reg[c[1]]
            else:
                reg[c[2]] = int(c[1])
            pos += 1
        elif c[0] == 'mul': # optimization to part 2
            if c[1] in reg:
                reg[c[2]] *= reg[c[1]]
            else:
                reg[c[2]] *= int(c[1])
            pos += 1
        elif c[0] == 'inc':
            reg[c[1]] += 1
            pos += 1
        elif c[0] == 'dec':
            reg[c[1]] -= 1
            pos += 1
        elif c[0] == 'jnz':
            if c[1] not in reg:
                check = int(c[1])
            else:
                check = reg[c[1]]
            if check:
                if c[2] in reg:
                    pos += reg[c[2]]
                else:
                    pos += int(c[2])
            else:
                pos += 1
        else: # tgl
            if c[1] not in reg:
                step = int(c[1])
            else:
                step = reg[c[1]]
            i = pos + step
            if i != pos and i < len(cmd):
                if cmd[i][0] == 'inc':
                    cmd[i][0] = 'dec'
                elif cmd[i][0] == 'jnz':
                    cmd[i][0] = 'cpy'
                elif len(cmd[i]) == 2:
                    cmd[i][0] = 'inc'
                else:
                    cmd[i][0] = 'jnz'
            pos += 1
    return reg['a']

print('Part 1:', simulate(7, deepcopy(cmd)))
print('Part 2:', simulate(12, deepcopy(cmd)))