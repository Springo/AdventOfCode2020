import time
from collections import deque


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d22input.txt")

switch = False
p1 = []
p2 = []
for line in lines[1:]:
    if not switch:
        if len(line) == 0:
            switch = True
        else:
            p1.append(int(line))
    else:
        if line.isnumeric():
            p2.append(int(line))



orig_p1 = p1[:]
orig_p2 = p2[:]

while len(p1) > 0 and len(p2) > 0:
    t1 = p1.pop(0)
    t2 = p2.pop(0)
    if t1 > t2:
        p1.append(t1)
        p1.append(t2)
    else:
        p2.append(t2)
        p2.append(t1)



score = 0
if len(p1) > 0:
    for i in range(len(p1)):
        score += (i + 1) * p1[-i - 1]
else:
    for i in range(len(p2)):
        score += (i + 1) * p2[-i - 1]
print(score)


def recursive_game(p1, p2, games):
    key = (tuple(p1), tuple(p2))
    if key in games:
        return games[key]

    seen = dict()

    while len(p1) > 0 and len(p2) > 0:
        winner = recursive_combat(p1, p2, seen, games)
        t1 = p1.popleft()
        t2 = p2.popleft()
        if winner == 1:
            p1.append(t1)
            p1.append(t2)
        else:
            p2.append(t2)
            p2.append(t1)

    if len(p1) > 0:
        games[key] = (1, p1)
        return 1, p1
    else:
        games[key] = (2, p2)
        return 2, p2


def recursive_combat(p1, p2, seen, games):
    if (tuple(p1), tuple(p2)) in seen:
        return 1

    seen[(tuple(p1), tuple(p2))] = True
    t1 = p1[0]
    t2 = p2[0]

    if len(p1) < t1 + 1 or len(p2) < t2 + 1:
        if t1 > t2:
            return 1
        else:
            return 2

    p1_new = deque(list(p1)[1:t1 + 1])
    p2_new = deque(list(p2)[1:t2 + 1])

    win, _ = recursive_game(p1_new, p2_new, games)
    return win


p1 = deque(orig_p1[:])
p2 = deque(orig_p2[:])
_, winner = recursive_game(p1, p2, dict())
score = 0
for i in range(len(winner)):
    score += (i + 1) * winner[-i - 1]
print(score)


