def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d21input.txt")


al_list = dict()
ing_lines = dict()
al_lines = dict()
for i in range(len(lines)):
    line = lines[i]
    ls1 = line.split(" (contains ")
    ings = ls1[0].split()
    algs = ls1[1][:-1].split(', ')
    for ing in ings:
        if ing not in ing_lines:
            ing_lines[ing] = []
        ing_lines[ing].append(i)
        for alg in algs:
            if alg not in al_list:
                al_list[alg] = set()
            al_list[alg].add(ing)
    for alg in algs:
        if alg not in al_lines:
            al_lines[alg] = []
        al_lines[alg].append(i)


for alg in al_list:
    rem_list = []
    for ing in al_list[alg]:
        for li in al_lines[alg]:
            if li not in ing_lines[ing]:
                rem_list.append(ing)
                break

    for ing in rem_list:
        al_list[alg].remove(ing)


invalid = dict()
for alg in al_list:
    for ing in al_list[alg]:
        invalid[ing] = True


total = 0
for ing in ing_lines:
    if ing not in invalid:
        total += len(ing_lines[ing])
print(total)


for iter in range(10):
    for alg in al_list:
        if len(al_list[alg]) == 1:
            bad_ing = list(al_list[alg])[0]
            for alg2 in al_list:
                if alg2 != alg and bad_ing in al_list[alg2]:
                    al_list[alg2].remove(bad_ing)


ans_list = []
for alg in al_list:
    ans_list.append((list(al_list[alg])[0], alg))

ans_list = sorted(ans_list, key=lambda tup: tup[1])
for a, b in ans_list:
    print("{},".format(a), end='')
