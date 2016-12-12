
def solve(initial_state, final_state):
    history_map = {}
    history_map[initial_state] = []
    unchecked_states = [initial_state]
    loop = 0
    while unchecked_states:
        loop += 1
        if loop % 10000 == 0:
            print "loop {}".format(loop)

        unchecked_state = unchecked_states.pop(0)
        next_states = get_next_states(unchecked_state)
        next_history = history_map[unchecked_state] + [unchecked_state]
        for next_state in next_states:
            if (
                (next_state not in history_map) or 
                (len(history_map[next_state]) > len(next_history))
            ):
                history_map[next_state] = next_history
                unchecked_states.append(next_state)
    
    return history_map[final_state]
   
def is_floor_state_ok(floor):
    microchips = tuple(i for i, v in enumerate(floor) if (i % 2 == 1) and v)
    generators = tuple(i for i, v in enumerate(floor) if (i % 2 == 0) and v)
    for microchip in microchips:
        has_shield = floor[microchip - 1]
        if not has_shield and len(generators) > 0:
            return False
    return True

assert is_floor_state_ok((0, 1, 0, 1))
assert is_floor_state_ok((1, 0, 1, 0))
assert is_floor_state_ok((1, 1, 1, 0))
assert not is_floor_state_ok((1, 1, 0, 1))

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

history = solve(initial_state, final_state)
for h in history:
    print h
print len(history)


def part_one():
    #The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
    #The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
    #The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
    #The fourth floor contains nothing relevant.
    # TH , PL , ST , PR , RU
    floor_0 = (1, 1, 1, 0, 1, 0, 0, 0, 0, 0)
    floor_1 = (0, 0, 0, 1, 0, 1, 0, 0, 0, 0)
    floor_2 = (0, 0, 0, 0, 0, 0, 1, 1, 1, 1)
    floor_3 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    initial_state = (0, (floor_0, floor_1, floor_2, floor_3))
    full_floor = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    empty_floor = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    final_state = (3, (empty_floor, empty_floor, empty_floor, full_floor))
    r = solve(initial_state, final_state)
    print len(r)

def part_two():
    floor_0 = (1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    floor_1 = (0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
    floor_2 = (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0)
    floor_3 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1)
    initial_state = (0, (floor_0, floor_1, floor_2, floor_3))
    full_floor = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    empty_floor = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    final_state = (3, (empty_floor, empty_floor, empty_floor, full_floor))
    r = solve(initial_state, final_state)
    print len(r)

part_two()