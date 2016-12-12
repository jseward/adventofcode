import re
from functools import partial
from collections import defaultdict


def cpy(x, y, state):
    try:
        state['registers'][y] = int(x)
    except ValueError:
        state['registers'][y] = state['registers'][x] 
    state['instruction'] += 1

def inc(x, state):
    state['registers'][x] += 1
    state['instruction'] += 1

def dec(x, state):
    state['registers'][x] -= 1
    state['instruction'] += 1

def jnz(x, y, state):
    try:
        is_not_zero = (int(x) != 0)
    except ValueError:
        is_not_zero = (state['registers'][x] != 0)

    if is_not_zero:
        try:
            state['instruction'] += int(y)
        except ValueError:
            state['instruction'] += state['registers'][y]
    else:
        state['instruction'] += 1

def parse_op(s):
    cpy_search = re.search("cpy (\S+) (\D+)", s)
    if cpy_search:
        return partial(cpy, cpy_search.group(1), cpy_search.group(2))

    inc_search = re.search("inc (\D+)", s)
    if inc_search:
        return partial(inc, inc_search.group(1))

    dec_search = re.search("dec (\D+)", s)
    if dec_search:
        return partial(dec, dec_search.group(1))

    jnz_search = re.search("jnz (\S+) (\S+)", s)
    if jnz_search:
        return partial(jnz, jnz_search.group(1), jnz_search.group(2))

    raise ValueError(s)

def run(op_strings, reg_init=None):
    ops = [parse_op(s) for s in op_strings]
    state = {
        "instruction": 0,
        "registers": defaultdict(int) 
    }

    if reg_init:
        for k, v in reg_init.iteritems():
            state['registers'][k] = v

    while state['instruction'] < len(ops):
        ops[state['instruction']](state)
    return state

def run_example():
    op_strings = [
        "cpy 41 a",
        "inc a",
        "inc a",
        "dec a",
        "jnz a 2",
        "dec a"
    ]
    print run(op_strings)

def run_part_1():
    with open('day12.input', 'rt') as f:
        op_strings = [line.strip() for line in f.readlines()]
    print run(op_strings) 

def run_part_2():
    with open('day12.input', 'rt') as f:
        op_strings = [line.strip() for line in f.readlines()]
    print run(op_strings, reg_init={'c': 1}) 

#run_example()
#run_part_1()
run_part_2()

