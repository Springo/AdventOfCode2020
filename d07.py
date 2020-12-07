def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def bfs(adj_list, key, target):
    explored = dict()
    q = [key]
    explored[key] = True
    while len(q) > 0:
        item = q.pop()
        for cur in adj_list[item]:
            _, id = cur
            if id == target:
                return True

            if id not in explored:
                q.append(id)
                explored[id] = True
    return False


def count_bags(adj_list, key):
    count = 1
    for cur in adj_list[key]:
        num, id = cur
        count += num * count_bags(adj_list, id)
    return count


lines = readFile("d07input.txt")

adj_list = dict()
rev_adj_list = dict()
for line in lines:
    args = line[:-1].split(" contain ")
    inside = args[1].split(", ")
    a = args[0].split()
    key = a[0] + " " + a[1]
    adj_list[key] = []
    for ins in inside:
        b = ins.split()
        if b[0] == "no":
            continue
        b_id = (int(b[0]), b[1] + " " + b[2])
        adj_list[key].append(b_id)
        if b_id not in adj_list:
            adj_list[b_id] = []

count = 0
for key in adj_list:
    if bfs(adj_list, key, "shiny gold"):
        count += 1
print(count)

print(count_bags(adj_list, "shiny gold") - 1)
