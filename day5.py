import hashlib
import operator

def make_password(door_id):
    index = 0
    password = ""
    while len(password) < 8:
        m = hashlib.md5()
        m.update(door_id)
        m.update(str(index))
        digest = m.hexdigest()
        if digest[:5] == "00000":
            password += digest[5]
            print "{} -> {}".format(index, password)
        index += 1
        if index % 100000 == 0:
            print "{} ...".format(index)
    return password

#print make_password("wtnhxymk")

def make_password_2(door_id):
    index = 0
    char_map = {}
    password = ""
    while len(password) < 8:
        m = hashlib.md5()
        m.update(door_id)
        m.update(str(index))
        digest = m.hexdigest()
        if digest[:5] == "00000":
            pos = digest[5]
            if (pos >= '0') and (pos < '8'):
                char = digest[6]
                if not (pos in char_map):
                    char_map[pos] = char
                sorted_chars = sorted(char_map.items(), key=operator.itemgetter(0))
                password = "".join([x[1] for x in sorted_chars])
                print "{} -> {} -> {}".format(index, sorted_chars, password)
        index += 1
        if index % 250000 == 0:
            print "{} ...".format(index)
    return password      

print make_password_2("wtnhxymk")
