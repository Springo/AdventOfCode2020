def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d04input.txt")

passes = []
new_pass = dict()
for line in lines:
    if len(line) <= 1:
        passes.append(new_pass)
        new_pass = dict()

    args = line.split()
    for arg in args:
        pair = arg.split(":")
        new_pass[pair[0]] = pair[1]
passes.append(new_pass)

valid = 0
need = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passp in passes:
    okay = True
    for ne in need:
        if ne not in passp:
            okay = False

    if okay:
        byr = int(passp['byr'])
        if byr < 1920 or byr > 2002:
            okay = False
            continue
        iyr = int(passp['iyr'])
        if iyr < 2010 or iyr > 2020:
            okay = False
            continue
        eyr = int(passp['eyr'])
        if eyr < 2020 or eyr > 2030:
            okay = False
            continue
        if passp['hgt'][-2:] != 'cm' and passp['hgt'][-2:] != 'in':
            okay = False
            continue
        else:
            hgt = int(passp['hgt'][:-2])
            if passp['hgt'][-2:] == 'cm':
                if hgt < 150 or hgt > 193:
                    okay = False
                    continue
            else:
                if hgt < 59 or hgt > 76:
                    okay = False
                    continue
        v_chars = "0123456789abcdef"
        if passp['hcl'][0] != '#' or len(passp['hcl']) != 7:
            okay = False
            continue
        for c in passp['hcl'][1:]:
            if c not in v_chars:
                okay = False

        v_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if passp['ecl'] not in v_eyes:
            okay = False
            continue

        v_chars = "0123456789"
        if len(passp['pid']) != 9:
            okay = False
        for c in passp['pid']:
            if c not in v_chars:
                okay = False

    if okay:
        valid += 1

print(valid)
