def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d13input.txt")

earliest = int(lines[0])
ls = lines[1].split(',')
ids = []
for l in ls:
    try:
        val = int(l)
        ids.append(val)
    except:
        continue


bus_id = None
waited = None
min_r = None
for id in ids:
    result = id - (earliest % id)
    if min_r is None or result < min_r:
        min_r = result
        bus_id = id
        waited = earliest + result

print(bus_id * min_r)


m_list = []
r_list = []
counter = 0
for l in ls:
    if l != 'x':
        m = int(l)
        r = (m - counter) % m
        m_list.append(m)
        r_list.append(r)
    counter += 1


def bezout(a, b):
    if a == 0:
        return b, 0, 1
    else:
        new_a = b % a
        new_b = a
        gcd, x, y = bezout(new_a, new_b)

        mult = b // a
        new_x = y - mult * x
        new_y = x
        return gcd, new_x, new_y


def mod_inv(a, m):
    a = a % m
    gcd, x, y = bezout(a, m)
    return x


def crt(r_list, m_list):
    cumul_r = r_list[0]
    cumul_m = m_list[0]
    for i in range(1, len(m_list)):
        r = r_list[i]
        m = m_list[i]
        A = mod_inv(m, cumul_m) * cumul_r * m + mod_inv(cumul_m, m) * r * cumul_m
        M = cumul_m * m
        cumul_r = A % M
        cumul_m = M

    return cumul_r


print(crt(r_list, m_list))
