import re

WIDTH = 50 
HEIGHT = 6 

def process_rect(screen, width, height):
    for y in xrange(height):
        for x in xrange(width):
            screen[y][x] = True 

def process_rotate_row(screen, y, shift):
    for i in xrange(shift):
        new_row = []
        for x in xrange(WIDTH):
            if x == 0:
                new_row.append(screen[y][WIDTH - 1])
            else:    
                new_row.append(screen[y][x - 1])
        screen[y] = new_row

def process_rotate_column(screen, x, shift):
    for i in xrange(shift):
        new_column = []
        for y in xrange(HEIGHT):
            if y == 0:
                new_column.append(screen[HEIGHT - 1][x])
            else:    
                new_column.append(screen[y - 1][x])
        for y in xrange(HEIGHT):
            screen[y][x] = new_column[y]

def process_instruction(screen, instruction):
    rect_search = re.search("rect (\d+)x(\d+)", instruction)
    if rect_search:
        width = int(rect_search.group(1))
        height = int(rect_search.group(2))
        process_rect(screen, width, height)
    
    rotate_row_search = re.search("rotate row y=(\d+) by (\d+)", instruction)
    if rotate_row_search:
        y = int(rotate_row_search.group(1))
        shift = int(rotate_row_search.group(2))
        process_rotate_row(screen, y, shift)

    rotate_column_search = re.search("rotate column x=(\d+) by (\d+)", instruction)
    if rotate_column_search:
        x = int(rotate_column_search.group(1))
        shift = int(rotate_column_search.group(2))
        process_rotate_column(screen, x, shift)

def process_instructions(instructions):
    screen = []
    for i in xrange(HEIGHT):
        screen.append([False for i in xrange(WIDTH)])

    for instruction in instructions:
        process_instruction(screen, instruction)
        #print ""
        #print instruction
        #print_screen(screen)        

    return screen

def print_screen(screen):
    for row in screen:
        print "".join(['#' if pixel else '.' for pixel in row])

#print_screen(process_instructions(["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"]))

with open('day8.input', 'rt') as f:
    raw_input = f.readlines()

screen = process_instructions(raw_input)

print_screen(screen)
print sum([1 if pixel else 0 for row in screen for pixel in row])