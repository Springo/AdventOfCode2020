def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d03input.txt")

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(c)
    grid.append(row)

total_trees = 1
trees = 0
for i in range(1, len(grid)):
    if grid[i][1 * i % len(grid[0])] == '#':
        trees += 1
total_trees = total_trees * trees

trees = 0
for i in range(1, len(grid)):
    if grid[i][3 * i % len(grid[0])] == '#':
        trees += 1
total_trees = total_trees * trees

trees = 0
for i in range(1, len(grid)):
    if grid[i][5 * i % len(grid[0])] == '#':
        trees += 1
total_trees = total_trees * trees

trees = 0
for i in range(1, len(grid)):
    if grid[i][7 * i % len(grid[0])] == '#':
        trees += 1
total_trees = total_trees * trees

trees = 0
for i in range(2, len(grid), 2):
    if grid[i][(i // 2) % len(grid[0])] == '#':
        trees += 1
total_trees = total_trees * trees

print(total_trees)
