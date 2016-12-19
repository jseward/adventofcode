from collections import deque


def inc_elf(elf, num_elves):
    inc_elf = elf + 1
    if inc_elf >= num_elves:
        inc_elf = 0
    return inc_elf

def get_next_elf_with_presents(have_presents, curr_elf):
    next_elf = inc_elf(curr_elf, len(have_presents))
    while next_elf != curr_elf:
        if have_presents[next_elf]:
            return next_elf
        next_elf = inc_elf(next_elf, len(have_presents))
    return None

def which_elf(num_elves):
    have_presents = [True for i in xrange(num_elves)]
    curr_elf = 0
    last_elf = None
    while curr_elf != None:
        #print "curr_elf = {}".format(curr_elf + 1)
        next_elf = get_next_elf_with_presents(have_presents, curr_elf)
        #print "{} taking from {}".format(curr_elf + 1, next_elf + 1)
        have_presents[next_elf] = False
        last_elf = curr_elf

        curr_elf = get_next_elf_with_presents(have_presents, curr_elf)

    return last_elf + 1

#print which_elf_2(5)
#print which_elf_2(3004953)

def which_elf_2(num_elves):
    have_presents = deque((i + 1) for i in xrange(num_elves))
    while len(have_presents) > 1:
        curr = have_presents.popleft()
        next = have_presents.popleft()
        have_presents.append(curr)
    return have_presents.pop()

print which_elf_2(5)
print which_elf_2(3004953)

