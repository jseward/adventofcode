def is_overlapped(a, b):
    return True if (b[0] >= a[0]) and ((b[0] - 1) <= a[1]) else False

assert is_overlapped((1,2), (3,5))

def get_sorted_merged_blocked(blocked):
    blocked = sorted(blocked, key=lambda x: x[0])
    
    merged = []
    m = None
    for b in blocked:
        if m is None:
            m = b
        else:
            if is_overlapped(m, b):
                m = (m[0], max(m[1], b[1]))
            else:
                merged.append(m)
                m = b
    if m:
        merged.append(m)

    return merged

def get_lowest_unblocked(blocked):
    merged = get_sorted_merged_blocked(blocked)
    assert merged[0][0] == 0
    return merged[0][1] + 1

with open('day20.input', 'rt') as f:
    raw_input = f.readlines()

def parse_blocked(s):
    s = s.strip()
    dash = s.index('-')
    begin = int(s[0:dash])
    end = int(s[dash + 1:])
    return (begin, end)

assert parse_blocked('123-789') == (123,789)

print get_lowest_unblocked([parse_blocked(x) for x in raw_input])
print get_lowest_unblocked([(5,8), (0,2), (4,7)])

def get_allowed_count(blocked, max_ip):
    merged = get_sorted_merged_blocked(blocked)
    count = 0
    for i, b in enumerate(merged):
        if i == (len(merged) - 1):
            count += max_ip - b[1]
        else:
            next_b = merged[i + 1]
            count += next_b[0] - b[1] - 1
    return count

print get_allowed_count([parse_blocked(x) for x in raw_input], 4294967295)
print get_allowed_count([(5,8), (0,2), (4,7)], 9)

