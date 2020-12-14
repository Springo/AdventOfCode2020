def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d14input.txt")


def maskover(val, mask):
    bval = list(str(bin(val))[2:])
    for i in range(len(mask)):
        c = mask[len(mask) - i - 1]
        if i >= len(bval):
            bval.insert(0, '0')

        if c == '0':
            bval[len(bval) - i - 1] = '0'
        elif c == '1':
            bval[len(bval) - i - 1] = '1'
    return int(''.join(bval), 2)


def maskover2(addr, mask):
    bval = list(str(bin(addr))[2:])
    pad = 36 - len(bval)
    padding = ['0'] * pad
    padding.extend(bval)
    bval = padding
    for i in range(len(mask)):
        c = mask[i]

        if c == '1':
            bval[i] = '1'
        elif c == 'X':
            bval[i] = 'X'

    addr_list = helper(bval)
    return addr_list


def helper(bval):
    for i in range(len(bval)):
        c = bval[i]
        if c == 'X':
            new_bval_0 = bval[:]
            new_bval_1 = bval[:]
            new_bval_0[i] = '0'
            new_bval_1[i] = '1'
            a_list_0 = helper(new_bval_0)
            a_list_1 = helper(new_bval_1)
            a_list_0.extend(a_list_1)
            return a_list_0
    return [int(''.join(bval), 2)]


ins = []
for line in lines:
    ls = line.split(" = ")
    ins.append(ls)

mask = 0
mem = dict()
for left, right in ins:
    if left == "mask":
        mask = right
    else:
        addr = int(left[4:-1])
        mem[addr] = maskover(int(right), mask)

total = 0
for key in mem:
    total += mem[key]
print(total)


mem = dict()
for left, right in ins:
    if left == "mask":
        mask = right
    else:
        addr = int(left[4:-1])
        val = int(right)
        addr_list = maskover2(addr, mask)
        for a in addr_list:
            mem[a] = val

total = 0
for key in mem:
    total += mem[key]
print(total)

