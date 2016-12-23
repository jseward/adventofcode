import re
from functools import partial
from collections import defaultdict


def is_register(x):
    try:
        x_int = int(x)
    except ValueError:
        return True
    return False

assert is_register('a')
assert not is_register('1')

VERBOSE = False
verbose_file = open('day23.output', 'wt') if VERBOSE else None

def is_verbose(state):
    return verbose_file

def state_to_string(state):
    return "a={} b={} c={} d={}".format(state['registers']['a'], state['registers']['b'], state['registers']['c'], state['registers']['d'])

def cpy(x, y, state, is_tgl):
    if is_tgl:
        jnz(x, y, state, False)
        return

    if not is_register(y):
        return

    try:
        value = int(x)
    except ValueError:
        value = state['registers'][x] 

    if is_verbose(state):
        verbose_file.write("{}: cpy {} ({}) -> {} : {}\n".format(state['instruction'], x, value, y, state_to_string(state)))

    state['registers'][y] = value
    state['instruction'] += 1

def inc(x, state, is_tgl):
    if is_tgl:
        dec(x, state, False)
        return

    state['registers'][x] += 1
    if is_verbose(state):
        verbose_file.write("{}: inc {} -> ({}) : {}\n".format(state['instruction'], x, state['registers'][x], state_to_string(state)))
    state['instruction'] += 1

def dec(x, state, is_tgl):
    if is_tgl:
        inc(x, state, False)
        return

    state['registers'][x] -= 1
    if is_verbose(state):
        verbose_file.write("{}: dec {} -> ({}) : {}\n".format(state['instruction'], x, state['registers'][x], state_to_string(state)))
    state['instruction'] += 1

def jnz(x, y, state, is_tgl):
    if is_tgl:
        cpy(x, y, state, False)
        return

    try:
        is_not_zero = (int(x) != 0)
    except ValueError:
        is_not_zero = (state['registers'][x] != 0)

    if is_verbose(state):
        verbose_file.write("{}: jnz {} {} {}: {}\n".format(state['instruction'], x, is_not_zero, y, state_to_string(state)))

    if is_not_zero:
        try:
            state['instruction'] += int(y)
        except ValueError:
            state['instruction'] += state['registers'][y]
    else:
        state['instruction'] += 1

def mul(x, y, state, is_tgl):
    assert not is_tgl
    assert is_register(x)
    assert is_register(y)

    state['registers'][x] *= state['registers'][y]
    state['instruction'] += 1

def nul(state, is_tgl):
    assert not is_tgl
    state['instruction'] += 1

def tgl(x, state, is_tgl):
    if is_tgl:
        inc(x, state, False)
        return

    try:
        value = int(x)
    except ValueError:
        value = state['registers'][x]
    
    tgl_instruction = state['instruction'] + value
    state['tgl'][tgl_instruction] = True

    if is_verbose(state):
        verbose_file.write("{}: tgl {} : {}\n".format(state['instruction'], value, state_to_string(state)))

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

    tgl_search = re.search("tgl (\S+)", s)
    if tgl_search:
        return partial(tgl, tgl_search.group(1))

    mul_search = re.search("mul (\S+) (\S+)", s)
    if mul_search:
        return partial(mul, mul_search.group(1), mul_search.group(2))

    nul_search = re.search("nul", s)
    if nul_search:
        return partial(nul)
        
    raise ValueError(s)

def run(op_strings, reg_init=None):
    ops = [parse_op(s) for s in op_strings]
    state = {
        "instruction": 0,
        "registers": defaultdict(int),
        "tgl": {} 
    }

    if reg_init:
        for k, v in reg_init.iteritems():
            state['registers'][k] = v

    while state['instruction'] < len(ops):
        is_tgl = state['tgl'].get(state['instruction'], False)
        #print state['instruction']
        ops[state['instruction']](state, is_tgl)
    return state

def run_example():
    op_strings = [
        "cpy 2 a",
        "tgl a",
        "tgl a",
        "tgl a",
        "cpy 1 a",
        "dec a",
        "dec a"
    ]
    print run(op_strings)

def run_part_1():
    with open('day23.input', 'rt') as f:
        op_strings = [line.strip() for line in f.readlines()]
    print run(op_strings, reg_init={'a': 7}) 

def run_part_2():
    with open('day23.part2.input', 'rt') as f:
        op_strings = [line.strip() for line in f.readlines()]
    print run(op_strings, reg_init={'a': 12}) 

#run_example()
#run_part_1()
run_part_2()

