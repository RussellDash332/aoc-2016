'''
F4 .  .  .  .  .  
F3 .  .  .  LG .  
F2 .  HG .  .  .  
F1 E  .  HM .  LM
'''

'''
F4 .   .   .   .   .   .   .   .   .   .   .
F3 .   .   .   .   .   .   .   .   .   .   .
F2 .   .  PoM  .   .   .  PrM  .   .   .   .
F1 E  PoG  .  TG  TM  PrG  .  RG  RM  CG  CM
'''

from copy import deepcopy
from collections import deque

sample_state = {
    1: {'HM', 'LM'},
    2: {'HG'},
    3: {'LG'},
    4: set()
}
initial_state = {
    1: {'PoG', 'ThG', 'ThM', 'PrG', 'RG', 'RM', 'CG', 'CM'},
    2: {'PoM', 'PrM'},
    3: set(),
    4: set()
}

class State:
    def __init__(self, state, elevator=1):
        self.state = state
        self.rev = {}
        for k in state:
            for o in state[k]:
                self.rev[o] = k
        self.elevator = elevator

    def tupify(self):
        return (tuple(sorted(self.rev.items())), self.elevator)

    def actions(self):
        a = []
        to_move = list(filter(lambda x: self.rev[x] == self.elevator, self.rev.keys()))
        for s1 in to_move:
            for dest_floor in list(filter(lambda x: abs(x - self.elevator) == 1, self.state.keys())):
                a.append(((s1,), dest_floor))
                for s2 in to_move:
                    if s1 != s2:
                        a.append(((s1, s2), dest_floor))
        return a

    def do(self, a): # a = ((..., ...), dest_floor)
        stuff, dest_floor = a
        new_state = State(state=deepcopy(self.state), elevator=dest_floor)
        for s in stuff:
            new_state.state[new_state.rev[s]].remove(s)
            new_state.state[dest_floor].add(s)
            new_state.rev[s] = dest_floor
        return new_state

    def is_valid(self):
        for check in self.state.values():
            microchips = list(filter(lambda x: x[-1] == 'M', check))
            gens = list(filter(lambda x: x[-1] == 'G', check))
            for m in microchips:
                for g in gens:
                    if m[:-1] != g[:-1] and m[:-1] + 'G' not in gens:
                        return False
        return True

    def is_terminal(self):
        return sum(map(lambda x: len(self.state[x]), [1, 2, 3])) == 0

def BFS(st, debug=False):
    q = deque([(State(st), 0)])
    visited = {State(st).tupify()}
    while q:
        s, d = q.popleft()
        if debug and (not q or q[0][1] == d + 1):
            print(f'Depth {d} handled')
        for a in s.actions():
            nxt = s.do(a)
            if nxt.is_terminal():
                return d + 1
            tup = nxt.tupify()
            if nxt.is_valid() and tup not in visited:
                visited.add(tup)
                q.append((nxt, d + 1))

# Will take a while
print('Part 1:', BFS(deepcopy(initial_state)))
initial_state[1] |= {'EG', 'EM', 'DG', 'DM'}
print('Part 2:', BFS(deepcopy(initial_state)))