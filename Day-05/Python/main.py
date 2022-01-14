from hashlib import md5

s = input()

i, p = 1, ''
while len(p) != 8:
    while not md5((s + str(i)).encode('utf-8')).hexdigest().startswith('00000'):
        i += 1
    p += md5((s + str(i)).encode('utf-8')).hexdigest()[5]
    i += 1
print("Part 1:", p)

i, p = 1, [None] * 8
while not all(p):
    while not md5((s + str(i)).encode('utf-8')).hexdigest().startswith('00000'):
        i += 1
    h = md5((s + str(i)).encode('utf-8')).hexdigest()
    try:
        if p[int(h[5])] == None:
            p[int(h[5])] = h[6]
    except:
        pass
    i += 1
print("Part 2:", ''.join(p))