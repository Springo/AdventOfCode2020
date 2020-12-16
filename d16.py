def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d16input.txt")


rules = dict()
line = lines.pop(0)
while len(line) > 0:
    ls = line.split(": ")
    key = ls[0]
    rules[key] = []
    lss = ls[1].split(" or ")
    for a in lss:
        b = a.strip()
        bs = b.split('-')
        bsint = (int(bs[0]), int(bs[1]))
        rules[key].append(bsint)
    line = lines.pop(0)


def is_valid(rules, val):
    valid = False
    for key in rules:
        rule = rules[key]
        for r1, r2 in rule:
            if r1 <= val <= r2:
                valid = True

    return valid


def is_valid_fields(rules, val):
    fields = []
    for key in rules:
        rule = rules[key]
        for r1, r2 in rule:
            if r1 <= val <= r2:
                fields.append(key)

    return set(fields)


line = lines.pop(0)
line = lines.pop(0)
mytick = [int(n) for n in line.split(',')]


line = lines.pop(0)
line = lines.pop(0)

inv_count = 0
valid_ticks = []
for line in lines:
    tick = [int(n) for n in line.split(',')]
    add_tick = True
    for val in tick:
        if not is_valid(rules, val):
            inv_count += val
            add_tick = False
    if add_tick:
        valid_ticks.append(tick)

print(inv_count)


field_list = []
for i in range(len(mytick)):
    newset = set(rules.keys())
    field_list.append(newset)

for tick in valid_ticks:
    for i in range(len(tick)):
        val = tick[i]
        fields = is_valid_fields(rules, val)
        field_list[i] = field_list[i].intersection(fields)


done = False
while not done:
    for i in range(len(field_list)):
        fields = field_list[i]
        if len(fields) == 1:
            field = list(fields)[0]
            for j in range(len(field_list)):
                fields2 = field_list[j]
                if i != j and field in fields2:
                    fields2.remove(field)
    """
    for key in rules.keys():
        contained = 0
        for fields in field_list:
            if key in fields:
                contained += 1
        if contained == 1:
            for i in range(len(field_list)):
                if key in field_list[i]:
                    field_list[i] = set([key])
    """

    new_done = True
    for fields in field_list:
        if len(fields) != 1:
            new_done = False
    done = new_done


answer = 1
for i in range(len(mytick)):
    field = list(field_list[i])[0]
    if "departure" in field:
        answer *= mytick[i]

print(answer)

