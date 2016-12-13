def is_wall(magic, x, y):
    assert x >= 0
    assert y >= 0
    u = (x * x) + (3 * x) + (2 * x * y) + y + (y*y)
    u += magic
    u_bin = format(u, 'b')
    num_bits = sum(int(i) for i in u_bin)
    return (num_bits % 2) == 1

def print_maze(magic, width, height):
    for y in xrange(height):
        print "".join("#" if is_wall(magic, x, y) else "." for x in xrange(width))

#print_maze(1364, 32, 40)

def get_neighbours(magic, curr_pos):
    x, y = curr_pos
    neighbours = [] 
    for delta_x, delta_y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx = x + delta_x
        ny = y + delta_y
        if nx >= 0 and ny >= 0 and not is_wall(magic, nx, ny):
            neighbours.append((nx, ny))
    return neighbours

def get_shortest_path(magic, begin, end):
    dist = {begin:0}
    stack = [begin]
    while end not in dist:
        curr_pos = stack.pop(0)
        neighbours = get_neighbours(magic, curr_pos)
        n_dist = dist[curr_pos] + 1
        for n in neighbours:
            if (n not in dist) or (n_dist < dist[n]):
                dist[n] = n_dist
                stack.append(n)
                
    return dist[end]

print get_shortest_path(10, (1, 1), (7, 4))
print get_shortest_path(1364, (1, 1), (31, 39))

def get_num_locations(magic, begin, max_dist):
    dist = {begin:0}
    stack = [begin]
    while stack:
        curr_pos = stack.pop(0)
        neighbours = get_neighbours(magic, curr_pos)
        n_dist = dist[curr_pos] + 1
        if n_dist <= max_dist:
            for n in neighbours:
                if (n not in dist) or (n_dist < dist[n]):
                    dist[n] = n_dist
                    stack.append(n)
            
    return len(dist)

print get_num_locations(1364, (1, 1), 50)
