import sys, re

rules = list(map(lambda x: x.strip(), sys.stdin))
d, o = {}, {}

new_rules = []
for r in rules:
    g = re.findall(r'value (\d+) goes to bot (\d+)', r)
    if g:
        d[int(g[0][1])] = sorted(d.get(int(g[0][1]), []) + [int(g[0][0])])
    else:
        new_rules.append(r)
rules = new_rules

while [17, 61] not in d.values():
    new_rules = []
    for r in rules:
        g = re.findall(r'bot (\d+) gives low to bot (\d+) and high to bot (\d+)', r)
        if g and len(d.get(int(g[0][0]), [])) == 2:
            d[int(g[0][1])] = sorted(d.get(int(g[0][1]), []) + [d[int(g[0][0])][0]])
            d[int(g[0][2])] = sorted(d.get(int(g[0][2]), []) + [d[int(g[0][0])][1]])
            del d[int(g[0][0])]
        else:
            new_rules.append(r)
    rules = new_rules

for k in d:
    if d[k] == [17, 61]:
        print("Part 1:", k)

while rules:
    new_rules = []
    for r in rules:
        g = re.findall(r'bot (\d+) gives low to bot (\d+) and high to bot (\d+)', r)
        if g and len(d.get(int(g[0][0]), [])) == 2:
            d[int(g[0][1])] = sorted(d.get(int(g[0][1]), []) + [d[int(g[0][0])][0]])
            d[int(g[0][2])] = sorted(d.get(int(g[0][2]), []) + [d[int(g[0][0])][1]])
            del d[int(g[0][0])]
        else:
            g = re.findall(r'bot (\d+) gives low to output (\d+) and high to bot (\d+)', r)
            if g and len(d.get(int(g[0][0]), [])) == 2:
                o[int(g[0][1])] = d[int(g[0][0])][0]
                d[int(g[0][2])] = sorted(d.get(int(g[0][2]), []) + [d[int(g[0][0])][1]])
                del d[int(g[0][0])]
            else:
                g = re.findall(r'bot (\d+) gives low to bot (\d+) and high to output (\d+)', r)
                if g and len(d.get(int(g[0][0]), [])) == 2:
                    d[int(g[0][1])] = sorted(d.get(int(g[0][1]), []) + [d[int(g[0][0])][0]])
                    o[int(g[0][2])] = d[int(g[0][0])][1]
                    del d[int(g[0][0])]
                else:
                    g = re.findall(r'bot (\d+) gives low to output (\d+) and high to output (\d+)', r)
                    if g and len(d.get(int(g[0][0]), [])) == 2:
                        o[int(g[0][1])] = d[int(g[0][0])][0]
                        o[int(g[0][2])] = d[int(g[0][0])][1]
                        del d[int(g[0][0])]
                    else:
                        new_rules.append(r)
    rules = new_rules
print("Part 2:", o[0] * o[1] * o[2])