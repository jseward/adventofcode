def get_distance_1(raw_input):
    input = [(x.strip()[0], int(x.strip()[1:])) for x in raw_input.split(",")]
    
    x = 0
    y = 0
    direction = 0
    for (rotation, distance) in input:
        
        # update direction
        if rotation == 'L':
            direction = direction - 1
            if direction < 0:
                direction = 3
        elif rotation == 'R':
            direction = direction + 1
            if direction > 3:
                direction = 0
        else:
            raise ValueError()
        
        if direction == 0:
            y += distance
        elif direction == 1:
            x += distance
        elif direction == 2:
            y -= distance
        elif direction == 3:
            x -= distance
        else:
            raise ValueError()
 
    return abs(x) + abs(y)

def get_distance_2(raw_input):
    input = [(x.strip()[0], int(x.strip()[1:])) for x in raw_input.split(",")]
    
    x = 0
    y = 0
    direction = 0
    coords = []
    first_dup = None
    for (rotation, distance) in input:
        
        # update direction
        if rotation == 'L':
            direction = direction - 1
            if direction < 0:
                direction = 3
        elif rotation == 'R':
            direction = direction + 1
            if direction > 3:
                direction = 0
        else:
            raise ValueError()
        
        for i in xrange(distance):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            else:
                raise ValueError()
            
            if not first_dup:
                if (x, y) in coords:
                    first_dup = (x, y)                                
                    print first_dup
            
            coords.append((x, y))

    return abs(first_dup[0]) + abs(first_dup[1])

print get_distance_1('R2, L3')
print get_distance_1('R2, R2, R2')
print get_distance_1('R5, L5, R5, R3')
print get_distance_2('R8, R4, R4, R8')

input = "L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5"

print get_distance_1(input)
print get_distance_2(input)
