def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d01input.txt")

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        for k in range(j + 1, len(lines)):
            num1 = int(lines[i])
            num2 = int(lines[j])
            num3 = int(lines[k])
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
