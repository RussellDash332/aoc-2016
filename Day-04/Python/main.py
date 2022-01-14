import sys, string

def caesar_cipher(shift, s):
    res = ''
    for z in s:
        if z in string.ascii_lowercase:
            res += chr(97 + (ord(z) - 97 + shift) % 26)
        else:
            res += z
    return res

ans = 0
for line in sys.stdin:
    line = line.strip()
    check = line[-6:-1]
    en = line[:-11]
    d = {}
    for l in en:
        if l != '-':
            d[l] = d.get(l, 0) + 1
    compare = ''.join(list(map(lambda x: x[0], sorted(d.items(), key=lambda x: (-x[1], x[0]))[:5])))
    if check == compare:
        shift = int(line[-10:-7])
        ans += shift
        if caesar_cipher(shift, en) == 'northpole-object-storage':
            ans2 = shift
print("Part 1:", ans)
print("Part 2:", ans2)