import graph_util as gu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d19input.txt")


rules = dict()
adj_list = dict()
mess = []
i = 0
rule_read = True
while i < len(lines):
    line = lines[i]
    if len(line) == 0:
        rule_read = False
        i += 1
        continue
    if rule_read:
        ls = line.split()
        key = int(ls[0][:-1])
        adj_list[key] = []
        rules[key] = []
        rule = []
        for c in ls[1:]:
            if c.isnumeric():
                rule.append(int(c))
                adj_list[key].append(int(c))
            elif c == '|':
                rules[key].append(tuple(rule))
                rule = []
            else:
                rules[key] = c[1:-1]
        if isinstance(rules[key], list):
            rules[key].append(rule)
    else:
        mess.append(line)
    i += 1


top_adj = gu.top_sort(adj_list)[::-1]
new_rules = dict()
for key in top_adj:
    if not isinstance(rules[key], list):
        new_rules[key] = [rules[key]]
    else:
        new_rules[key] = []
        for args in rules[key]:
            str_list = []
            if len(args) == 1:
                str_list = new_rules[args[0]]
            else:
                l1 = new_rules[args[0]]
                l2 = new_rules[args[1]]
                for s1 in l1:
                    for s2 in l2:
                        str_list.append(s1 + s2)

            new_rules[key].extend(str_list)
            new_rules[key] = list(set(new_rules[key]))


valid_0 = dict()
for m in new_rules[0]:
    valid_0[m] = True
total = 0
for m in mess:
    if m in valid_0:
        total += 1
print(total)

valid_42 = dict()
for m in new_rules[42]:
    valid_42[m] = True
valid_31 = dict()
for m in new_rules[31]:
    valid_31[m] = True

len_val = 8


def check_valid_8(line, v42):
    if len(line) < 1:
        return False
    if len(line) % len_val != 0:
        return False
    for i in range(len(line) // len_val):
        substr = line[len_val * i: len_val * (i + 1)]
        if substr not in v42:
            return False
    return True


def check_valid_11(line, v42, v31):
    if len(line) < 1:
        return False
    if len(line) % (2 * len_val) != 0:
        return False
    for i in range(len(line) // (2 * len_val)):
        s1 = line[len_val * i: len_val * (i + 1)]
        i1 = len(line) - len_val * (i + 1)
        i2 = len(line) - len_val * i
        s2 = line[i1:i2]
        if s1 not in v42:
            return False
        if s2 not in v31:
            return False
    return True


total = 0
for m in mess:
    if len(m) % len_val == 0:
        v = False
        for i in range(len(m) // (2 * len_val)):
            cut = len(m) - ((2 * len_val) * (i + 1))
            s1 = m[:cut]
            s2 = m[cut:]
            if check_valid_8(s1, valid_42) and check_valid_11(s2, valid_42, valid_31):
                v = True
        if v:
            total += 1

print(total)
