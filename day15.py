disk_mods = [13, 5, 17, 3, 7, 19, 11]
disk_positions = [11, 0, 11, 0, 2, 17, 0]

time = 0

while True:
    disks_open = True
    for i in xrange(len(disk_positions)):
        if ((disk_positions[i] + time + i + 1) % disk_mods[i]) != 0:
            disks_open = False
            break

    if disks_open:
        print "TIME = {}".format(time)
        break
            
    time += 1




#Disc #1 has 13 positions; at time=0, it is at position 11.
#Disc #2 has 5 positions; at time=0, it is at position 0.
#Disc #3 has 17 positions; at time=0, it is at position 11.
#Disc #4 has 3 positions; at time=0, it is at position 0.
#Disc #5 has 7 positions; at time=0, it is at position 2.
#Disc #6 has 19 positions; at time=0, it is at position 17.


