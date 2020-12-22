
def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_borders(tile):
    up = tile[0]
    down = tile[-1]
    left = [tile[i][0] for i in range(10)]
    right = [tile[i][-1] for i in range(10)]
    rev_up = up[::-1]
    rev_down = down[::-1]
    rev_left = left[::-1]
    rev_right = right[::-1]
    return [up, right, down, left, rev_up, rev_right, rev_down, rev_left]


lines = readFile("d20input.txt")

tiles = dict()
for i in range(len(lines) // 12):
    ls = lines[i * 12].split()
    id = int(ls[1][:-1])
    grid = []
    for j in range(i * 12 + 1, i * 12 + 11):
        row = []
        for c in lines[j]:
            row.append(c)
        grid.append(row)
    tiles[id] = grid


orient = ['U', 'R', 'D', 'L', '-U', '-R', '-D', '-L']
blist = []
for tile in tiles:
    borders = get_borders(tiles[tile])
    for b in range(len(borders)):
        blist.append((tile, borders[b], orient[b]))


adj_list = dict()
for tile in tiles:
    adj_list[tile] = dict()
    for o in orient:
        adj_list[tile][o] = []
    borders = get_borders(tiles[tile])
    for k in range(len(borders)):
        border = borders[k]
        for b in blist:
            other_tile, other_b, other_or = b
            if other_tile != tile and other_b == border:
                adj_list[tile][orient[k]].append(b)

ans = 1
first = 0
for id in adj_list:
    total_bord = 0
    for ori in adj_list[id]:
        total_bord += len(adj_list[id][ori])
    if total_bord == 4:
        ans *= id
        first = id
print(ans)


def rot_tile(tile, rot):
    res = tile
    for r in range(rot):
        new_tile = []
        for i in range(len(tile)):
            row = [res[len(tile) - j - 1][i] for j in range(len(tile))]
            new_tile.append(row)
        res = new_tile
    return res


def flip_tile(tile):
    new_tile = []
    for row in tile:
        new_tile.append(row[::-1])
    return new_tile


image = []
image_ids = []
id_list1 = [first]
row1 = [tiles[first]]
b_ind_last = 'R'
for j in range(11):
    o_id, _, o_ori = adj_list[id_list1[-1]][b_ind_last][0]
    id_list1.append(o_id)
    if o_ori == 'L':
        row1.append(tiles[o_id])
        b_ind_last = 'R'
    elif o_ori == 'D':
        row1.append(rot_tile(tiles[o_id], 1))
        b_ind_last = 'U'
    elif o_ori == '-R':
        row1.append(rot_tile(tiles[o_id], 2))
        b_ind_last = '-L'
    elif o_ori == '-U':
        row1.append(rot_tile(tiles[o_id], 3))
        b_ind_last = '-D'
    elif o_ori == 'R':
        row1.append(flip_tile(tiles[o_id]))
        b_ind_last = 'L'
    elif o_ori == 'U':
        row1.append(flip_tile(rot_tile(tiles[o_id], 1)))
        b_ind_last = 'D'
    elif o_ori == '-L':
        row1.append(flip_tile(rot_tile(tiles[o_id], 2)))
        b_ind_last = '-R'
    elif o_ori == '-D':
        row1.append(flip_tile(rot_tile(tiles[o_id], 3)))
        b_ind_last = '-U'

image.append(row1)
image_ids.append(id_list1)

last_above = first
above_ind_last = 'D'
for i in range(11):
    row = []
    id_list = []

    o_id, _, o_ori = adj_list[last_above][above_ind_last][0]
    id_list.append(o_id)
    last_above = o_id
    if o_ori == 'U':
        row.append(tiles[o_id])
        above_ind_last = 'D'
        b_ind_last = 'R'
    elif o_ori == '-L':
        row.append(rot_tile(tiles[o_id], 1))
        above_ind_last = '-R'
        b_ind_last = 'U'
    elif o_ori == '-D':
        row.append(rot_tile(tiles[o_id], 2))
        above_ind_last = '-U'
        b_ind_last = '-L'
    elif o_ori == 'R':
        row.append(rot_tile(tiles[o_id], 3))
        above_ind_last = 'L'
        b_ind_last = '-D'
    elif o_ori == '-U':
        row.append(flip_tile(tiles[o_id]))
        above_ind_last = '-D'
        b_ind_last = 'L'
    elif o_ori == 'L':
        row.append(flip_tile(rot_tile(tiles[o_id], 1)))
        above_ind_last = 'R'
        b_ind_last = 'D'
    elif o_ori == 'D':
        row.append(flip_tile(rot_tile(tiles[o_id], 2)))
        above_ind_last = 'U'
        b_ind_last = '-R'
    elif o_ori == '-R':
        row.append(flip_tile(rot_tile(tiles[o_id], 3)))
        above_ind_last = '-L'
        b_ind_last = '-U'


    for j in range(11):
        o_id, _, o_ori = adj_list[id_list[-1]][b_ind_last][0]
        id_list.append(o_id)
        if o_ori == 'L':
            row.append(tiles[o_id])
            b_ind_last = 'R'
        elif o_ori == 'D':
            row.append(rot_tile(tiles[o_id], 1))
            b_ind_last = 'U'
        elif o_ori == '-R':
            row.append(rot_tile(tiles[o_id], 2))
            b_ind_last = '-L'
        elif o_ori == '-U':
            row.append(rot_tile(tiles[o_id], 3))
            b_ind_last = '-D'
        elif o_ori == 'R':
            row.append(flip_tile(tiles[o_id]))
            b_ind_last = 'L'
        elif o_ori == 'U':
            row.append(flip_tile(rot_tile(tiles[o_id], 1)))
            b_ind_last = 'D'
        elif o_ori == '-L':
            row.append(flip_tile(rot_tile(tiles[o_id], 2)))
            b_ind_last = '-R'
        elif o_ori == '-D':
            row.append(flip_tile(rot_tile(tiles[o_id], 3)))
            b_ind_last = '-U'

    image.append(row)
    image_ids.append(id_list)



real_image = []
for im_row in range(len(image)):
    for i in range(1, 9):
        row = []
        for im_col in range(len(image[im_row])):
            for j in range(1, 9):
                row.append(image[im_row][im_col][i][j])
        real_image.append(row)




def check_monster(off_row, off_col, img):
    mon_points = [(0, 18),
                  (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
                  (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
    for i, j in mon_points:
        if img[off_row + i][off_col + j] != '#' and img[off_row + i][off_col + j] != 'O':
            return False

    for i, j in mon_points:
        img[off_row + i][off_col + j] = 'O'
    return True


for flip in range(2):
    for rot in range(4):
        mons = 0

        for i in range(len(real_image) - 2):
            for j in range(len(real_image[i]) - 19):
                if check_monster(i, j, real_image):
                    mons += 1
        real_image = rot_tile(real_image, 1)
    real_image = flip_tile(real_image)

real_image = flip_tile(rot_tile(real_image, 1))

total = 0
for row in real_image:
    for c in row:
        if c == '#':
            total += 1
print(total)
