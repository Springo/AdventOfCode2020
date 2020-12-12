def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def move_coords(x, y, dir, steps):
    if dir == 0:
        return x + steps, y
    if dir == 1:
        return x, y - steps
    if dir == 2:
        return x - steps, y
    if dir == 3:
        return x, y + steps



lines = readFile("d12input.txt")

ins = []
for line in lines:
    com = line[0]
    amt = int(line[1:])
    ins.append((com, amt))



dir = 0
x = 0
y = 0
for com, amt in ins:
    if com == 'N':
        y += amt
    elif com == 'S':
        y -= amt
    elif com == 'E':
        x += amt
    elif com == 'W':
        x -= amt
    elif com == 'L':
        dir = (dir - (amt // 90)) % 4
    elif com == 'R':
        dir = (dir + (amt // 90)) % 4
    elif com == 'F':
        x2, y2 = move_coords(x, y, dir, amt)
        x = x2
        y = y2

print(abs(x) + abs(y))


def rotate_left(x, y, deg):
    x2 = x
    y2 = y
    for i in range(deg):
        temp = x2
        x2 = -y2
        y2 = temp
    return x2, y2


def rotate_right(x, y, deg):
    x2 = x
    y2 = y
    for i in range(deg):
        temp = x2
        x2 = y2
        y2 = -temp
    return x2, y2



x = 0
y = 0
wpx = 10
wpy = 1
for com, amt in ins:
    if com == 'N':
        wpy += amt
    elif com == 'S':
        wpy -= amt
    elif com == 'E':
        wpx += amt
    elif com == 'W':
        wpx -= amt
    elif com == 'L':
        x2, y2 = rotate_left(wpx, wpy, amt // 90)
        wpx = x2
        wpy = y2
    elif com == 'R':
        x2, y2 = rotate_right(wpx, wpy, amt // 90)
        wpx = x2
        wpy = y2
    elif com == 'F':
        x += wpx * amt
        y += wpy * amt

print(abs(x) + abs(y))
