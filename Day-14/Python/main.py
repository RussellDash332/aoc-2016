from hashlib import md5

def has_triple(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]
    return False

def has_quintuple(s):
    for i in range(len(s) - 5):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4]:
            return s[i]
    return False

def stretch(s):
    for _ in range(2016):
        s = md5(s.encode('utf-8')).hexdigest()
    return s

s = input()

def simulate(f):
    i, k = 0, 0
    quints = {}
    while k != 64:
        while not has_triple(md5(f(s + str(i)).encode('utf-8')).hexdigest()):
            i += 1
        check = has_triple(md5(f(s + str(i)).encode('utf-8')).hexdigest())
        found = False
        for j in range(1000):
            if i + j + 1 not in quints:
                quints[i + j + 1] = has_quintuple(md5(f(s + str(i + j + 1)).encode('utf-8')).hexdigest())
            if quints[i + j + 1] == check:
                found = True
                break
        if found:
            k += 1
        i += 1
    return i - 1

print('Part 1:', simulate(lambda x: x))
print('Part 2:', simulate(stretch))