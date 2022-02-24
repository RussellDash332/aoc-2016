import sys, string

letters = string.ascii_lowercase

cmd = []
for line in sys.stdin:
    cmd.append(line.strip().split())

def simulate(cval):
    reg, pos = {}, 0
    for k in 'abcd':
        reg[k] = 0
    reg['c'] = cval
    while pos < len(cmd):
        c = cmd[pos]
        if c[0] == 'cpy':
            if c[1] in reg:
                reg[c[2]] = reg[c[1]]
            else:
                reg[c[2]] = int(c[1])
            pos += 1
        elif c[0] == 'inc':
            reg[c[1]] += 1
            pos += 1
        elif c[0] == 'dec':
            reg[c[1]] -= 1
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
    return reg['a']

print('Part 1:', simulate(0))
print('Part 2:', simulate(1))