from functools import partial
import re


def swap_position(x, y, input):
    output = list(input)
    output[x] = input[y]
    output[y] = input[x]
    return ''.join(output)

assert swap_position(1, 2, 'abcd') == 'acbd'
assert swap_position(1, 2, 'acbd') == 'abcd' #reverse

def swap_letter(x, y, input):
    output = list(input)
    for i, _ in enumerate(output):
        if output[i] == x:
            output[i] = y
        elif output[i] == y:
            output[i] = x
    return ''.join(output)

assert swap_letter('c', 'b', 'abcd') == 'acbd'
assert swap_letter('c', 'b', 'acbd') == 'abcd' #reverse

def rotate_once(dir, input):
    assert dir in ['left', 'right']
    delta = 1 if dir == 'left' else -1
    output = ""
    for i, _ in enumerate(input):
        output += input[(i + delta) % len(input)]
    return output

def rotate(dir, num_steps, input):
    output = input[:]
    for i in xrange(num_steps):
        output = rotate_once(dir, output)
    return output

assert rotate('right', 1, 'abcd') == 'dabc'
assert rotate('left', 1, 'dabc') == 'abcd'

def rotate_by_position(x, input):
    index = input.index(x)
    num_steps = 1 + index + (1 if (index >= 4) else 0)
    return rotate('right', num_steps, input)

assert rotate_by_position('h', 'abcdefgh') == 'habcdefg'
assert rotate_by_position('a', 'abcdefgh') == 'habcdefg'
assert rotate_by_position('e', 'abcdefgh') == 'cdefghab'

def rotate_by_position_reverse(x, input):
    index = input.index(x)
    r = None
    if index == 0:
        r = ('right', 7)
    elif index == 1:
        r = ('left', 1)
    elif index == 2:
        r = ('right', 2)
    elif index == 3:
        r = ('left', 2)
    elif index == 4:
        r = ('right', 1)
    elif index == 5:
        r = ('left', 3)
    elif index == 6:
        pass
    elif index == 7:
        r = ('left', 4)        
    else:
        raise ValueError(index)
    
    if r:
        return rotate(r[0], r[1], input)
    else:
        return input

def reverse_positions(x, y, input):
    output = list(input)
    num_chars = y - x + 1
    for i in xrange(num_chars):
        output[x + i] = input[x + num_chars - 1 - i]
    return ''.join(output)

assert reverse_positions(1, 2, 'abcd') == 'acbd'
assert reverse_positions(1, 2, 'acbd') == 'abcd' #reverse

def move_position(x, y, input):
    output = input[0:x] + input[x+1:]
    output = output[0:y] + input[x] + output[y:]
    return output

assert move_position(1, 2, 'abcd') == 'acbd'
assert move_position(2, 1, 'acbd') == 'abcd' #reverse

def parse_op(op_string, reverse=False):
    swap_position_search = re.search("swap position (\d+) with position (\d+)", op_string)
    if swap_position_search:
        return partial(swap_position, int(swap_position_search.group(1)), int(swap_position_search.group(2)))

    swap_letter_search = re.search("swap letter (\w) with letter (\w)", op_string)
    if swap_letter_search:
        return partial(swap_letter, swap_letter_search.group(1), swap_letter_search.group(2))

    rotate_search = re.search("rotate (left|right) (\d+) step", op_string)
    if rotate_search:
        dir = rotate_search.group(1)
        if reverse:
            dir = 'left' if dir == 'right' else 'right'
        return partial(rotate, dir, int(rotate_search.group(2)))

    rotate_by_position_search = re.search("rotate based on position of letter (\w)", op_string)
    if rotate_by_position_search:
        if reverse:
            return partial(rotate_by_position_reverse, rotate_by_position_search.group(1))
        else:            
            return partial(rotate_by_position, rotate_by_position_search.group(1))

    reverse_search = re.search("reverse positions (\d+) through (\d+)", op_string)
    if reverse_search:
        return partial(reverse_positions, int(reverse_search.group(1)), int(reverse_search.group(2)))

    move_search = re.search("move position (\d+) to position (\d+)", op_string)
    if move_search:
        if not reverse:
            return partial(move_position, int(move_search.group(1)), int(move_search.group(2)))
        else:
            return partial(move_position, int(move_search.group(2)), int(move_search.group(1)))

    raise ValueError(op_string)

assert parse_op('rotate left 2 steps') != None

def scramble(op_strings, passcode):
    for op in [parse_op(x.strip()) for x in op_strings]:
        passcode = op(passcode)
    return passcode

def unscramble(op_strings, passcode):
    for op in reversed([parse_op(x.strip(), reverse=True) for x in op_strings]):
        passcode = op(passcode)
    return passcode


with open('day21.input', 'rt') as f:
    raw_input = f.readlines()

example_op_strings = [
    'swap position 4 with position 0',
    'swap letter d with letter b',
    'reverse positions 0 through 4',
    'rotate left 1 step',
    'move position 1 to position 4',
    'move position 3 to position 0',
    'rotate based on position of letter b',
    'rotate based on position of letter d'
]

#print scramble(example_op_strings, 'abcde')

#print scramble(raw_input, 'abcdefgh')
#print unscramble(raw_input, 'gbhafcde')

print unscramble(raw_input, 'fbgdceah')
