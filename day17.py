import hashlib

def get_next_coord(coord, dir):
    if dir == 'U':
        next_coord = (coord[0], coord[1] - 1)
    elif dir == 'D':
        next_coord = (coord[0], coord[1] + 1)
    elif dir == 'L':
        next_coord = (coord[0] - 1, coord[1])
    elif dir == 'R':
        next_coord = (coord[0] + 1, coord[1])
    
    if next_coord[0] < 0 or next_coord[0] > 3 or next_coord[1] < 0 or next_coord[1] > 3:
        return None
    return next_coord

def get_next(passcode, coord, path):
    md5 = hashlib.md5()
    md5.update(passcode + "".join(path))
    hash = md5.hexdigest()

    next = []
    dirs = ['U', 'D', 'L', 'R']
    open = 'bcdef'
    for i, dir in enumerate(dirs):
        if hash[i] in open:
            next_coord = get_next_coord(coord, dir)
            if next_coord:
                next.append((next_coord, dir))

    return next

def get_shortest_path(passcode):
    initial_coord = (0, 0)
    final_coord = (3, 3)
    paths = {(initial_coord, 0):[]}

    next_uid = 0
    current = [(initial_coord, next_uid)]
    next = []
    step = 0
    final_uid = 0
    path_lens = []
    while current:
        for coord, uid in current:
            path = paths[(coord, uid)]                

            if coord == final_coord:
                path_lens.append(len(path))
            else:
                coord_next = get_next(passcode, coord, path)
                for next_coord, next_dir in coord_next:
                    next_uid += 1
                    new_path = path[:]
                    new_path.append(next_dir)
                    paths[(next_coord, next_uid)] = new_path
                    next.append((next_coord, next_uid))

        current = next
        next = []
        step += 1

    #return ''.join(paths[(final_coord, final_uid)])
    return max(path_lens)

#print get_shortest_path('ihgpwlah')
#print get_shortest_path('kglvqrro')

print get_shortest_path('veumntbg')
