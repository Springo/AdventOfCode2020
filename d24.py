from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d24input.txt")


flipped = dict()
for line in lines:
    ins = []
    i = 0
    while i < len(line):
        if line[i] == 'e' or line[i] == 'w':
            ins.append(line[i])
            i += 1
        else:
            ins.append(line[i:i+2])
            i += 2

    y = 0
    x = 0
    for s in ins:
        if s[-1] == 'e':
            y -= 1
            if len(s) == 1:
                y -= 1
            elif s[0] == 'n':
                x += 1
            elif s[0] == 's':
                x -= 1

        elif s[-1] == 'w':
            y += 1
            if len(s) == 1:
                y += 1
            elif s[0] == 'n':
                x += 1
            elif s[0] == 's':
                x -= 1

    if (x, y) not in flipped:
        flipped[(x, y)] = False
    flipped[(x, y)] = not flipped[(x, y)]

total = 0
for flip in flipped:
    if flipped[flip]:
        total += 1
print(total)


neighbs = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 2), (0, -2)]
for iter in range(100):
    adj_tiles = dict()
    new_flipped = deepcopy(flipped)
    for flip in flipped:
        if flipped[flip]:
            x, y = flip
            for neigh in neighbs:
                new_x, new_y = neigh
                new_x = new_x + x
                new_y = new_y + y
                adj_tiles[(new_x, new_y)] = adj_tiles.get((new_x, new_y), 0) + 1

    for flip in flipped:
        if flipped[flip]:
            if flip not in adj_tiles or adj_tiles[flip] > 2:
                new_flipped[flip] = False

    for tile in adj_tiles:
        if tile not in flipped or not flipped[tile]:
            if adj_tiles[tile] == 2:
                new_flipped[tile] = True

    flipped = new_flipped


total = 0
for flip in flipped:
    if flipped[flip]:
        total += 1
print(total)
