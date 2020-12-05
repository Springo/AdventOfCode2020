def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d05input.txt")

inps = []
for line in lines:
    first = ""
    for c in line[:7]:
        if c == "F":
            first = first + "0"
        else:
            first = first + "1"

    last = ""
    for c in line[7:]:
        if c == "L":
            last = last + "0"
        else:
            last = last + "1"

    inps.append((first, last))

highest = 0
id_list = []
for inp in inps:
    f, l = inp
    row = int(f, 2)
    col = int(l, 2)
    id = row * 8 + col
    if id > highest:
        highest = id
    id_list.append(id)

print(highest)

id_list = sorted(id_list)
for i in range(813):
    if i not in id_list:
        print(i)

