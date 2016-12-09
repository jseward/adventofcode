
def is_valid_triangle(sides):
    assert(len(sides) == 3)
    combinations = [
        (0, 1, 2),
        (1, 0, 2),
        (2, 0, 1)]
    for (i, j, k) in combinations:
        if sides[i] >= (sides[j] + sides[k]):
            return False
    return True

with open('day3.input', 'rt') as f:
    raw_input = f.readlines()

input = []
for line in raw_input:
    input.append([int(x.strip()) for x in line.split(" ") if len(x.strip()) > 0])

valid_triangles = [i for i in input if is_valid_triangle(i)]

print "input = {}".format(len(input))
print "valid = {}".format(len(valid_triangles))

assert(len(input) % 3 == 0)

num_column_valid = 0

for c in xrange(3):
    i = 0
    while i < len(input):
        if is_valid_triangle((input[i][c], input[i + 1][c], input[i + 2][c])):
            num_column_valid += 1
        i += 3

print "valid_column = {}".format(num_column_valid)


