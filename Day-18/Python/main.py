def check_trap(l, c, r):
    return ''.join([l, c, r]) in ['^^.', '.^^', '^..', '..^']

m = [list(input())]
for _ in range(400000 - 1):
    temp = []
    for i in range(len(m[-1])):
        if i == 0:
            temp.append('.^'[int(check_trap('.', m[-1][i], m[-1][i + 1]))])
        elif i == len(m[-1]) - 1:
            temp.append('.^'[int(check_trap(m[-1][i - 1], m[-1][i], '.'))])
        else:
            temp.append('.^'[int(check_trap(m[-1][i - 1], m[-1][i], m[-1][i + 1]))])
    m.append(temp)

print('Part 1:', sum(map(lambda x: x.count('.'), m[:40])))
print('Part 2:', sum(map(lambda x: x.count('.'), m)))