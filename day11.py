
def solve(initial_state, final_state):
    state_to_num_moves_map = {}
    solve_recursive(state_to_num_moves_map, initial_state, 0)
    print len(state_to_num_moves_map)
    return state_to_num_moves_map[final_state]

def solve_recursive(state_to_num_moves_map, state, num_moves):
    next_num_moves = num_moves + 1
    for next_state in get_next_states(state):
        if (next_state not in state_to_num_moves_map) or (state_to_num_moves_map[next_state] > next_num_moves):
            state_to_num_moves_map[next_state] = next_num_moves
            solve_recursive(state_to_num_moves_map, next_state, next_num_moves)
            
def is_floor_state_ok(floor):
    microchips = tuple(i for i, v in enumerate(floor) if (i % 2 == 0) and v)
    generators = tuple(i for i, v in enumerate(floor) if (i % 2 == 1) and v)
    for microchip in microchips:
        has_shield = floor[microchip - 1]
        if not has_shield and len(generators) > 0:
            return False
    return True

def make_floor_state(indices, length):
    return tuple(1 if i in indices else 0 for i in xrange(length))

def attempt_append_next_state(next_states, state, elevator_state, delta):
    elevator, floors = state
    next_elevator = elevator + delta
    if next_elevator < 0 or next_elevator >= len(floors):
        return
    next_floor_state = tuple(
        1 if (elevator_state[i] or floors[next_elevator][i]) else 0 
        for i in xrange(len(elevator_state))
    )
    prev_floor_state = tuple(
        1 if (not elevator_state[i] and floors[elevator][i]) else 0
        for i in xrange(len(elevator_state))
    )
    if is_floor_state_ok(next_floor_state) and is_floor_state_ok(prev_floor_state):
        def get_next_floor_state(i, f):
            if i == elevator:
                return prev_floor_state
            elif i == next_elevator:
                return next_floor_state
            return f
        next_floors = tuple(
            get_next_floor_state(i, f)
            for i, f in enumerate(floors)
        )
        next_states.append((next_elevator, next_floors))

def get_next_states(state):
    elevator, floors = state
    current_floor = floors[elevator]
    assert is_floor_state_ok(current_floor)
    elevator_states = []
    for i, iv in enumerate(current_floor):
        if iv:
            elevator_states.append(make_floor_state((i, ), len(current_floor)))
            for j, jv in enumerate(current_floor):
                if (j > i) and jv:
                    combo_state = make_floor_state((i, j), len(current_floor))
                    if is_floor_state_ok(combo_state):
                        elevator_states.append(combo_state)
    next_states = []
    for elevator_state in elevator_states:
        attempt_append_next_state(next_states, state, elevator_state, -1)
        attempt_append_next_state(next_states, state, elevator_state, +1)
    return next_states

initial_state = (0, (
    (0, 1, 0, 1),
    (1, 0, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 0)
))
final_state = (3, (
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (1, 1, 1, 1)
))

print solve(initial_state, final_state)


#The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
#The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
#The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
#The fourth floor contains nothing relevant.
#loor_0 = [(GENERATOR, "TH"), (MICROCHIP, "TH"), (GENERATOR, "PL"), (GENERATOR, "ST")]
#floor_1 = [(MICROCHIP, "PL"), (MICROCHIP, "ST")]
#floor_2 = [(GENERATOR, "PR"), (MICROCHIP, "PR"), (GENERATOR, "RU"), (MICROCHIP, "RU")]
#floor_3 = []
#print solve([floor_0, floor_1, floor_2, floor_3])


