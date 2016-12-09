def decompress(input):
    output = ""

    i = 0
    while i < len(input):
        if input[i] == '(':
            x_pos = input.find("x", i)
            close_pos = input.find(")", x_pos)
            num_chars = int(input[i + 1:x_pos])
            num_repeats = int(input[x_pos + 1:close_pos]) 
            chars_to_repeat = input[close_pos + 1:close_pos + 1 + num_chars]
            output += "".join([chars_to_repeat for n in xrange(num_repeats)])
            i = close_pos + 1 + num_chars

        else:
            output += input[i]
            i += 1

    return output

print decompress("ADVENT")
print decompress("A(1x5)BC")
print decompress("(3x3)XYZ")
print decompress("A(2x2)BCD(2x2)EFG")
print decompress("(6x1)(1x3)A")
print decompress("X(8x2)(3x3)ABCY")

raw_input = open('day9.input', 'rt').read()
print len(decompress(raw_input))

def get_decompress_len_recursive(depth, input):
    #print "{}:{}".format(depth, input)
    decompress_len = 0
    i = 0
    while i < len(input):
        if input[i] == '(':
            x_pos = input.find("x", i)
            close_pos = input.find(")", x_pos)
            num_chars = int(input[i + 1:x_pos])
            num_repeats = int(input[x_pos + 1:close_pos]) 
            chars_to_repeat = input[close_pos + 1:close_pos + 1 + num_chars]
            chars_to_repeat_len = get_decompress_len_recursive(depth + 1, chars_to_repeat)
            decompress_len += (chars_to_repeat_len * num_repeats)
            i = close_pos + 1 + num_chars

        else:
            decompress_len += 1
            i += 1

    return decompress_len

print get_decompress_len_recursive(0, "X(8x2)(3x3)ABCY")
print get_decompress_len_recursive(0, "(27x12)(20x12)(13x14)(7x10)(1x12)A")
print get_decompress_len_recursive(0, "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")
print get_decompress_len_recursive(0, raw_input)



