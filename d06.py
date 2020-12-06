def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d06input.txt")

total1 = 0
total2 = 0
stored = dict()
peeps = 0
for line in lines:
    if len(line) == 0:
        total1 += len(stored.keys())
        for key in stored:
            if stored[key] == peeps:
                total2 += 1
        stored = dict()
        peeps = 0
        continue

    peeps += 1
    for c in line:
        if c not in stored:
            stored[c] = 0
        stored[c] += 1

total1 += len(stored.keys())
for key in stored:
    if stored[key] == peeps:
        total2 += 1

print(total1)
print(total2)
