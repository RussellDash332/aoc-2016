import sys, re, string

def contains_abba(s):
    if len(s) < 4: return False
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False

ans, ans2 = 0, 0
for line in sys.stdin:
    words = (set(re.findall(r'[a-z]*(?=\[)', line.strip())) | set(re.findall(r'(?<=\])[a-z]*', line.strip()))) - {''}
    hypernet = re.findall(r'\[([a-z]*)\]', line.strip())
    ans += int(any(map(contains_abba, words)) and not any(map(contains_abba, hypernet)))

    def do():
        for a in string.ascii_lowercase:
            for b in string.ascii_lowercase:
                for w in words:
                    for h in hypernet:
                        if a + b + a in w and b + a + b in h:
                            return 1
        return 0

    ans2 += do()
print("Part 1:", ans)
print("Part 2:", ans2)