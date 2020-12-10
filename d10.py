def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d10input.txt")

vals = []
for line in lines:
    vals.append(int(line))

counter = dict()
counter[1] = 0
counter[2] = 0
counter[3] = 1
vals = sorted(vals)
counter[vals[0]] += 1
for i in range(len(vals) - 1):
    diff = vals[i + 1] - vals[i]
    counter[diff] += 1
print(counter[1] * counter[3])

totals = [0] * len(vals)
totals[0] = 1
totals[1] = 2
totals[2] = 4
for i in range(3, len(vals)):
    totals[i] = totals[i - 1]
    if vals[i] - 3 <= vals[i - 2]:
        totals[i] += totals[i - 2]
    if vals[i] - 3 <= vals[i - 3]:
        totals[i] += totals[i - 3]
print(totals[len(vals) - 1])

