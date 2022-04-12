bits = input()

def simulate(bits, length):
    while len(bits) < length:
        bits = bits + '0' + ''.join(map(lambda x: str(1 - int(x)), bits[::-1]))
    bits = bits[:length]
    while len(bits) % 2 == 0:
        temp = []
        for i in range(len(bits) // 2):
            if bits[2*i] == bits[2*i + 1]:
                temp.append('1')
            else:
                temp.append('0')
        bits = ''.join(temp)
    return bits

print('Part 1:', simulate(bits, 272))
print('Part 2:', simulate(bits, 35651584))