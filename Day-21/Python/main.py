import sys
from itertools import permutations

cmd = []
for line in sys.stdin:
    cmd.append(line)

def simulate(s):
    for line in cmd:
        line2 = line
        line = line.strip().split()
        if line2.startswith('swap position'):
            x, y = int(line[2]), int(line[-1])
            s[x], s[y] = s[y], s[x]
        elif line2.startswith('swap letter'):
            x, y = s.index(line[2]), s.index(line[-1])
            s[x], s[y] = s[y], s[x]
        elif line2.startswith('rotate based'):
            x = s.index(line[-1])
            steps = (x + 1 + int(x >= 4)) % len(s)
            s = s[-steps:] + s[:-steps]
        elif line2.startswith('rotate left'):
            steps = int(line[2]) % len(s)
            s = s[steps:] + s[:steps]
        elif line2.startswith('rotate right'):
            steps = int(line[2]) % len(s)
            s = s[-steps:] + s[:-steps]
        elif line2.startswith('reverse positions'):
            x, y = int(line[2]), int(line[-1])
            s[x:y+1] = s[x:y+1][::-1]
        else: # move position
            x, y = int(line[2]), int(line[-1])
            s.insert(y, s.pop(x))
    return ''.join(s)

print('Part 1:', simulate(list('abcdefgh')))
for s in list(map(list, permutations('abcdefgh'))):
    if simulate(s) == 'fbgdceah':
        print('Part 2:', ''.join(s))
        break