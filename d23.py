inp = "624397158"


def crab_move(num_list, iters):
    cap = len(num_list)
    next_num = dict()
    for i in range(len(num_list)):
        next_num[num_list[i]] = num_list[(i + 1) % cap]

    cur = num_list[0]
    for iter in range(iters):
        c1 = next_num[cur]
        c2 = next_num[c1]
        c3 = next_num[c2]
        next_cur = next_num[c3]
        dest = ((cur - 2) % cap) + 1
        while dest == c1 or dest == c2 or dest == c3:
            dest = ((dest - 2) % cap) + 1
        next_num[cur] = next_cur
        temp = next_num[dest]
        next_num[dest] = c1
        next_num[c3] = temp
        cur = next_cur

    return next_num


inp = [int(c) for c in inp]
p1 = crab_move(inp, 100)

ans = p1[1]
while ans != 1:
    print(ans, end='')
    ans = p1[ans]
print()

inp.extend([i for i in range(10, 1000001)])
p2 = crab_move(inp, 10 ** 7)
print(p2[1] * p2[p2[1]])


