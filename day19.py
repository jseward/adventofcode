from collections import deque

def which_elf_1(num_elves):
    have_presents = deque((i + 1) for i in xrange(num_elves))
    while len(have_presents) > 1:
        curr = have_presents.popleft()
        next = have_presents.popleft()
        have_presents.append(curr)
    return have_presents.pop()

#print which_elf_1(5)
#print which_elf_1(3004953)

def balance(hp0, hp1):
    # balance the two groups of elves so
    # that the end of hp0 is who to steal from.
    total = len(hp0) + len(hp1)
    n = 2 if total % 2 == 0 else 1
    while len(hp0) - n != len(hp1):
        hp0.append(hp1.popleft())

def which_elf_2(num_elves):
    n = (num_elves / 2)
    hp0 = deque((i + 1) for i in xrange(n))
    hp1 = deque((i + n + 1) for i in xrange(num_elves - n))
    balance(hp0, hp1)
    while len(hp1) > 0:
        hp1.append(hp0.popleft())
        hp0.pop()
        balance(hp0, hp1)

    return hp0.popleft()

print which_elf_2(5)
print which_elf_2(7)
print which_elf_2(3004953)

