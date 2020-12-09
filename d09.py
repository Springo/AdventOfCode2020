def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def twosum(l, val):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == val:
                return True
    return False


lines = readFile("d09input.txt")


v_sums = []
vs = []
count = 0
done = False
for line in lines:
    v = int(line)
    vs.append(v)
    count += 1

    if count > 25 and not done:
        if not twosum(vs[count - 26:-1], v):
            print(v)
            done = True

inv = 31161678
ind1 = 0
ind2 = 2

while True:
    new_l = vs[ind1:ind2]
    su = sum(new_l)
    if su == inv:
        print(max(new_l) + min(new_l))
        break
    if su < inv:
        ind2 += 1
    else:
        ind1 += 1

