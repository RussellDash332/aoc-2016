puzzle = input()

def decompose(puzzle, rec):
    if '(' not in puzzle:
        return len(puzzle)
    
    pos = puzzle.find('(')
    end = puzzle.find(')') + 1
    mul = puzzle[pos + 1:end - 1]
    size, rep = list(map(int, mul.split('x')))
    if rec:
        return pos + decompose(puzzle[end:end + size], True) * rep + decompose(puzzle[end + size:], True)
    else:
        return pos + len(puzzle[end:end + size]) * rep + decompose(puzzle[end + size:], False)

print("Part 1:", decompose(puzzle, False))
print("Part 2:", decompose(puzzle, True))