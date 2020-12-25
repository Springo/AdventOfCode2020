key1 = 6270530
key2 = 14540258


def mod_log(b, res, m):
    cur = 1
    ex = 0
    while cur != res:
        cur = (cur * b) % m
        ex += 1
    return ex


def mod_exp(b, exp, m):
    b = b % m

    result = 1
    prev = b
    while exp > 0:
        if exp % 2 == 1:
            result = (result * prev) % m
        exp = exp // 2
        prev = (prev * prev) % m

    return result


loop_size_1 = mod_log(7, key1, 20201227)
loop_size_2 = mod_log(7, key2, 20201227)

print(loop_size_1)
print(loop_size_2)

print(mod_exp(key1, loop_size_2, 20201227))
print(mod_exp(key2, loop_size_1, 20201227))


