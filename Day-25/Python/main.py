import sys, string

letters = string.ascii_lowercase

cmd = []
for line in sys.stdin:
    cmd.append(line.strip().split())

def simulate(aval):
    res = []
    reg, pos = {}, 0
    for k in 'abcd':
        reg[k] = 0
    reg['a'] = aval
    while len(res) != 12 and pos < len(cmd):
        c = cmd[pos]
        if c[0] == 'cpy':
            if c[1] in reg:
                reg[c[2]] = reg[c[1]]
            else:
                reg[c[2]] = int(c[1])
            pos += 1
        elif c[0] == 'add': # optimization
            if c[1] in reg:
                reg[c[2]] += reg[c[1]]
            else:
                reg[c[2]] += int(c[1])
            pos += 1
        elif c[0] == 'inc':
            reg[c[1]] += 1
            pos += 1
        elif c[0] == 'dec':
            reg[c[1]] -= 1
            pos += 1
        elif c[0] == 'out':
            if c[1] in reg:
                res.append(reg[c[1]])
            else:
                res.append(int(c[1]))
            pos += 1
        else: # jnz
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
    return ''.join(map(str, res))[::-1]

check = 0
while int(simulate(check), 2) != int('10'*6, 2):
    check += 1
print('Part 1:', check)
print('Part 2: THE END!')