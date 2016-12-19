def make_tile(prev_row, i):
    prev_traps = (
        False if (i - 1) < 0 else prev_row[i - 1],
        prev_row[i],
        False if (i + 1) >= len(prev_row) else prev_row[i + 1])

    return prev_traps in [
        (True, True, False),
        (False, True, True),
        (True, False, False),
        (False, False, True)]

def make_row(prev_row):
    return [make_tile(prev_row, i) for i in xrange(len(prev_row))]

def parse_row(s):
    return [True if c == '^' else False for c in s]

def count_safe(initial_row, num_rows):
    rows = [parse_row(initial_row)]
    while len(rows) < num_rows:
        if len(rows) % 10000 == 0:
            print len(rows)
        rows.append(make_row(rows[-1]))
    
    num_safe = 0
    for r in rows:
        for t in r:
            num_safe += 0 if t else 1
    return num_safe

def count_safe_2(initial_row, num_rows):
    prev_row = parse_row(initial_row)
    n = 0
    num_safe = 0
    while(n < num_rows):
        num_safe += sum(0 if t else 1 for t in prev_row)
        prev_row = make_row(prev_row)
        n += 1
    return num_safe

print count_safe_2('.^^.^.^^^^', 10)

input = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
print count_safe_2(input, 40)

print count_safe_2(input, 400000)
