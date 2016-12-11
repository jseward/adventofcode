GENERATOR = 'g'
MICROCHIP = 'm'

def can_exist(items):
    microchips = [i for i in items if i[0] == MICROCHIP]
    generators = [i for i in items if i[0] == GENERATOR]
    for microchip in microchips:
        has_shield = any(i for i in generators if i[1] == microchip[1])
        if not has_shield:
            return len(generators) > 0
    return True

def get_possible_moves(floors, elevator, prev_move):
    all_combos = []
    for i, item in enumerate(floors[elevator]):
        all_combos.append([item])
        for other_item in floors[elevator][i + 1:]:
            combo = [item, other_item]
            if can_exist(combo):
                all_combos.append(combo)

    possible_moves = []
    for combo in all_combos:
        
        def add_possible_move_if_valid(delta):
            next_elevator = elevator + delta
            if next_elevator >= 0 and next_elevator < len(floors):
                if can_exist(combo + floors[next_elevator]):
                    move = (combo, delta)
                    if not prev_move or move != (prev_move[0], -prev_move[1]):
                        possible_moves.append(move)
        
        add_possible_move_if_valid(-1)
        add_possible_move_if_valid(+1)

    return possible_moves

def get_move_score(move):
    items, delta = move
    has_generator = any(i for i in items if i[0] == GENERATOR)
    if delta > 0:
        return (1000 if has_generator else 100) * len(items)
    else:
        return (0 if has_generator else 10) * len(items)                

def solve(floors):
    count = 0
    elevator = 0
    total_num_items = sum([len(floor) for floor in floors])
    prev_move = None
    while len(floors[len(floors) - 1]) < total_num_items:
        possible_moves = get_possible_moves(floors, elevator, prev_move)
        sorted_moves = sorted(possible_moves, key=get_move_score, reverse=True)
        #print sorted_moves
        move = sorted_moves[0]
        print move
        floors[elevator] = [i for i in floors[elevator] if i not in move[0]]
        elevator += move[1]
        floors[elevator] = floors[elevator] + move[0]
        prev_move = move
        count += 1

    return count

print solve([
    [(MICROCHIP, 'H'), (MICROCHIP, 'L')],
    [(GENERATOR, 'H')],
    [(GENERATOR, 'L')],
    []
])

#The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
#The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
#The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
#The fourth floor contains nothing relevant.
floor_0 = [(GENERATOR, "TH"), (MICROCHIP, "TH"), (GENERATOR, "PL"), (GENERATOR, "ST")]
floor_1 = [(MICROCHIP, "PL"), (MICROCHIP, "ST")]
floor_2 = [(GENERATOR, "PR"), (MICROCHIP, "PR"), (GENERATOR, "RU"), (MICROCHIP, "RU")]
floor_3 = []
#print solve([floor_0, floor_1, floor_2, floor_3])


