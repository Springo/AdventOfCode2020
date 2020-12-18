def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d18input.txt")


def parse_line(line, order=False):
    num_list = []
    op_list = []
    ind = 0
    while ind < len(line):
        c = line[ind]
        if c.isnumeric():
            num_list.append(int(c))
        elif c == ' ':
            ind += 1
            continue
        elif c == '+' or c == '*':
            op_list.append(c)
        elif c == '(':
            par_count = 1
            done = False
            ind2 = ind
            while not done:
                ind2 += 1
                if line[ind2] == '(':
                    par_count += 1
                if line[ind2] == ')':
                    if par_count > 1:
                        par_count -= 1
                    else:
                        done = True
            num_list.append(parse_line(line[ind + 1: ind2], order=order))
            ind = ind2 - 1
        ind += 1

    prev_val = 1
    cur_val = num_list[0]
    num_ind = 1
    op_ind = 0
    while num_ind < len(num_list):
        op = op_list[op_ind]
        op_ind += 1
        if op == '+':
            cur_val += num_list[num_ind]
            num_ind += 1
        elif op == '*':
            if order:
                prev_val *= cur_val
                cur_val = num_list[num_ind]
                num_ind += 1
            else:
                cur_val *= num_list[num_ind]
                num_ind += 1
    prev_val = prev_val * cur_val
    return prev_val


total = 0
for line in lines:
    total += parse_line(line, order=False)

print(total)

total = 0
for line in lines:
    total += parse_line(line, order=True)

print(total)
