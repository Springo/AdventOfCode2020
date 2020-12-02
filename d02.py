def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d02input.txt")

valid = 0
for line in lines:
    ins = line.split()
    valid_range = ins[0].split('-')
    r1 = int(valid_range[0])
    r2 = int(valid_range[1])

    pass_char = ins[1][:-1]
    passw = ins[2]
    c_count = dict()
    for c in passw:
        if c not in c_count:
            c_count[c] = 0
        c_count[c] += 1

    if pass_char not in c_count:
        c_count[pass_char] = 0

    counter = 0
    if passw[r1 - 1] == pass_char:
        counter += 1
    if passw[r2 - 1] == pass_char:
        counter += 1

    # if r1 <= c_count[pass_char] <= r2:
    if counter == 1:
        valid += 1

print(valid)
