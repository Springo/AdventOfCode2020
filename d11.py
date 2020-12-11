from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def serialize(grid):
    stuff = ""
    for row in grid:
        for c in row:
            stuff = stuff + c
    return stuff


def grid_project(grid, i, j, dir, step=1):
    if dir == 0:
        if j < len(grid[i]) - step:
            return i, j + step
    elif dir == 1:
        if i < len(grid) - step and j < len(grid[i]) - step:
            return i + step, j + step
    elif dir == 2:
        if i < len(grid) - step:
            return i + step, j
    elif dir == 3:
        if i < len(grid) - step and j >= step:
            return i + step, j - step
    elif dir == 4:
        if j >= step:
            return i, j - step
    elif dir == 5:
        if i >= step and j >= step:
            return i - step, j - step
    elif dir == 6:
        if i >= step:
            return i - step, j
    elif dir == 7:
        if i >= step and j < len(grid[i]) - step:
            return i - step, j + step
    return None, None


def get_neigh(grid, i, j):
    neigh = []
    for dir in range(8):
        i2, j2 = grid_project(grid, i, j, dir)
        if i2 is not None:
            neigh.append(grid[i2][j2])
    return neigh


def get_seen(grid, i, j):
    seen = []

    for dir in range(8):
        done = False
        step = 1
        while not done:
            i2, j2 = grid_project(grid, i, j, dir, step=step)
            if i2 is None:
                done = True
            elif grid[i2][j2] == '#' or grid[i2][j2] == 'L':
                seen.append(grid[i2][j2])
                done = True
            else:
                step += 1

    return seen


def count_seat(neigh):
    count = 0
    for n in neigh:
        if n == "#":
            count += 1
    return count


lines = readFile("d11input.txt")

grid = []
for line in lines:
    l = []
    for c in line:
        l.append(c)
    grid.append(l)

seen = dict()
seen[serialize(grid)] = True

done = False
while not done:
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #neigh = get_neigh(grid, i, j)
            neigh = get_seen(grid, i, j)
            count = count_seat(neigh)
            if grid[i][j] == "L" and count == 0:
                new_grid[i][j] = '#'
            #if grid[i][j] == "#" and count >= 4:
            if grid[i][j] == "#" and count >= 5:
                new_grid[i][j] = 'L'
    ser = serialize(new_grid)
    if ser in seen:
        done = True
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    total += 1
        print(total)
    seen[ser] = True
    grid = new_grid
