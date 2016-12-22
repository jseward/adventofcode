def is_viable_pair(nodes, a, b):
    a_used, a_avail = nodes[a]
    b_used, b_avail = nodes[b]

    return (a != b) and (a_used > 0) and (a_used <= b_avail)

def get_neighbours(width, height, x, y):
    neighbours = []
    for d_x, d_y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        n_x = x + d_x
        n_y = y + d_y
        if (n_x >= 0) and (n_x < width) and (n_y >= 0) and (n_y < height):
            neighbours.append((n_x, n_y))
    return neighbours

def get_num_viable_pairs(nodes):
    num_viable_pairs = 0
    for a_coord in nodes.iterkeys():
        for b_coord in nodes.iterkeys():
            if is_viable_pair(nodes, a_coord, b_coord):
                num_viable_pairs += 1
    return num_viable_pairs

with open('day22.input', 'rt') as f:
    raw_input = f.readlines()

def parse_input(x):
    import re

    search = re.search('/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T', x)
    if search:
        return (
            int(search.group(1)),
            int(search.group(2)),
            int(search.group(4)),
            int(search.group(5))
        )
    
    raise ValueError(x)

assert parse_input('/dev/grid/node-x0-y0     92T   72T    20T   78%') == (0, 0, 72, 20)

nodes = {}
for x, y, used, avail in [parse_input(x) for x in raw_input]:
    nodes[(x, y)] = (used, avail)

#print get_num_viable_pairs(nodes)

def print_nodes(nodes):
    def to_char(node):
        used, avail = node
        if used == 0:
            return '_'
        if used > 100:
            return '#'
        else:
            return '.'

    width = max(x for x, _ in nodes.iterkeys()) + 1
    height = max(y for _, y in nodes.iterkeys()) + 1

    for y in xrange(height):
        print '{} {}'.format(y, ''.join(to_char(nodes[(x, y)]) for x in xrange(width)))
            
print_nodes(nodes)
