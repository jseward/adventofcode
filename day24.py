from collections import deque


def make_graph(map):
    graph = {}
    values = []
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == '#':
                pass
            elif char == '.':
                graph[(x, y)] = None
            else:
                graph[(x, y)] = int(char)
                values.append(int(char))
    return graph, values

def get_neightbour_coords(graph, coord):
    n_coords = []
    x, y = coord
    for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n_coord = (x + delta_x, y + delta_y)
        if n_coord in graph:
            n_coords.append(n_coord)
    return n_coords

def shortest_pair(graph, pair):
    a, b = pair
    a_coord = graph.keys()[graph.values().index(a)]
    b_coord = graph.keys()[graph.values().index(b)]

    dg = {a_coord: (0, [])}

    q = deque()
    q.append(a_coord)
    while q and (b_coord not in dg):
        curr_coord = q.popleft()
        for n_coord in get_neightbour_coords(graph, curr_coord):
            if n_coord not in dg:
                curr_dist, curr_other_values = dg[curr_coord]
                n_other_values = curr_other_values
                if graph[n_coord] != None and n_coord != b_coord:
                     n_other_values = n_other_values[:]
                     n_other_values.append(graph[n_coord])
                dg[n_coord] = (curr_dist + 1, n_other_values)
                q.append(n_coord)
            else:
                pass
                #assert dg[n_coord][0] <= dg[curr_coord][0]

    return dg[b_coord]

def make_pairs(graph, values):
    pairs = []
    for x in values:
        for y in values:
            if x != y:
                pairs.append((x, y))
    
    pairs_dict = { p: shortest_pair(graph, p) for p in pairs }
    # hack just to simplify later search (have both directions in dict)
    for k, v in pairs_dict.iteritems():
        pairs_dict[(k[1], k[0])] = v
    return pairs_dict

def is_chain_complete(pairs, chain):
    values = {}
    for v0, v1 in pairs.iterkeys():
        values[v0] = True
        values[v1] = True

    for c in chain:
        values[c[0]] = False
        values[c[1]] = False

    is_chain_complete = True
    for k, v in values.iteritems():
        if v:
            is_chain_complete = False
    return is_chain_complete

def is_chain_complete_2(pairs, chain):
    return is_chain_complete(pairs, chain) and (chain[-1][1] == 0)

def calc_chain_dist(pairs, chain):
    dist = 0
    for c in chain:
        dist += pairs[c][0]
    return dist

def value_not_in_chain(chain, value):
    for c in chain:
        if value == c[0] or value == c[1]:
            return False
    return True

def next_chain_potential_pairs(pairs, chain):
    last_pair = chain[-1]
    if not is_chain_complete(pairs, chain):
        return [p for p in pairs.iterkeys() if (p[0] == last_pair[1]) and value_not_in_chain(chain, p[1])]
    else:
        return [(last_pair[1], 0)]

def eval_shortest_pairs(pairs):
    incomplete_chains = deque([p] for p in pairs.iterkeys() if p[0] == 0)
    chains = []
    while incomplete_chains:
        c = incomplete_chains.pop()
        potential_pairs = next_chain_potential_pairs(pairs, c)
        for p in potential_pairs:
            new_chain = c[:]
            new_chain.append(p)
            if is_chain_complete_2(pairs, new_chain):
                chains.append(new_chain)
            else:
                incomplete_chains.append(new_chain)
    
    shortest_chain = None
    for c in chains:
        dist = calc_chain_dist(pairs, c)
        if not shortest_chain or (dist < calc_chain_dist(pairs, shortest_chain)):
            shortest_chain = c

    return (shortest_chain, calc_chain_dist(pairs, shortest_chain))


def run_example():
    map = [
        "###########",
        "#0.1.....2#",
        "#.#######.#",
        "#4.......3#",
        "###########"
    ]
    graph, values = make_graph(map)
    pairs = make_pairs(graph, values)
    shortest = eval_shortest_pairs(pairs)
    #for k, v in pairs.iteritems():
    #    print "{} : {}".format(k, v)
    for v in shortest:
        print "{}".format(v)

def run_part_1():
    with open('day24.input', 'rt') as f:
        map = [x.strip() for x in f.readlines()]
    graph, values = make_graph(map)
    pairs = make_pairs(graph, values)
    #for k, v in pairs.iteritems():
    #    print "{} : {}".format(k, v)
    shortest = eval_shortest_pairs(pairs)
    for v in shortest:
        print "{}".format(v)

#run_example()
run_part_1()
