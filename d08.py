def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def execute(ins, stop_loop=False):
    acc = 0
    i = 0
    found = dict()
    found[0] = True
    while i < len(ins):
        com, num = ins[i]
        if com == "acc":
            acc += num
        elif com == "jmp":
            i += num - 1
        i += 1
        if i in found:
            if found[i] == 2:
                return -1
            else:
                if stop_loop:
                    return acc
                found[i] += 1
        else:
            found[i] = 0

    return acc


lines = readFile("d08input.txt")

ins = []
for line in lines:
    ls = line.split()
    a = ls[0]
    sign = ls[1][0]
    b = int(ls[1][1:])
    if sign == '-':
        b = -b
    ins.append((a, b))

print(execute(ins, True))


for i in range(len(ins)):
    com, num = ins[i]
    if com == "jmp":
        new_ins = ins[:]
        new_ins[i] = ("nop", num)
        val = execute(new_ins)
        if val != -1:
            print(val)
