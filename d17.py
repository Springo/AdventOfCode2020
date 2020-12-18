import time

def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def print_grid(grid):
    keys = grid.keys()
    x = []
    y = []
    layers = []
    for i, j, k in keys:
        y.append(i)
        x.append(j)
        layers.append(k)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)

    lay = sorted(list(set(layers)))
    for l in lay:
        print("Layer {}".format(l))
        for i in range(ymin, ymax + 1):
            for j in range(xmin, xmax + 1):
                if (i, j, l) in grid:
                    print(grid[(i, j, l)], end='')
                else:
                    print('.', end='')
            print()


t1 = time.time()
lines = readFile("d17input.txt")
#lines = readFile("test.txt")


grid = dict()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[(i, j, 0, 0)] = lines[i][j]


for iter in range(6):
    new_neighbs = dict()
    for key in grid:
        i, j, k, w = key
        if grid[key] == '#':
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        for d in range(3):
                            i2 = i + a - 1
                            j2 = j + b - 1
                            k2 = k + c - 1
                            w2 = w + d - 1
                            if i2 != i or j2 != j or k2 != k or w2 != w:
                                new_neighbs[(i2, j2, k2, w2)] = new_neighbs.get((i2, j2, k2, w2), 0) + 1

    for key in new_neighbs:
        if key not in grid or grid[key] == '.':
            if new_neighbs[key] == 3:
                grid[key] = '#'
        else:
            if new_neighbs[key] != 2 and new_neighbs[key] != 3:
                grid[key] = '.'

    for key in grid:
        if key not in new_neighbs:
            grid[key] = '.'


total = 0
for key in grid:
    if grid[key] == '#':
        total += 1
print(total)

t2 = time.time()
print(t2 - t1)

