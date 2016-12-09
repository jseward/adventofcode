def parse_room(s):
    ts = s.strip()
    name = ts[:ts.rfind('-')]
    rest = ts[len(name) + 1:]
    sector = int(rest[:rest.find('[')])
    checksum = rest[rest.find('[') + 1:len(rest) - 1]
    return (name, sector, checksum)

def make_checksum(name):
    from collections import defaultdict
    num_chars = defaultdict(int)
    for c in name:
        if c != '-':
            num_chars[c] += 1
    
    def char_cmp(a, b):
        result = cmp(a[1], b[1])
        if result == 0:
            result = cmp(b[0], a[0])
        return result
         
    num_chars_sorted = sorted(num_chars.iteritems(), cmp=char_cmp, reverse=True)
    return "".join([c[0] for c in num_chars_sorted[:5]])

def is_checksum_valid(room):
    return make_checksum(room[0]) == room[2] 

def get_sector_sum(room_strings):
    rooms = [parse_room(s) for s in room_strings]
    valid_rooms = [r for r in rooms if is_checksum_valid(r)]
    return sum([r[1] for r in valid_rooms])

def get_decrypted_name(room):
    encrypted_name, sector, _ = room
    alpha_chars = "abcdefghijklmnopqrstuvwxyz"
    decrypted_name = ""
    for c in encrypted_name:
        if c == '-':
            decrypted_name += ' '
        else:    
            enc_i = alpha_chars.find(c)
            dec_i = (enc_i + sector) % len(alpha_chars)
            decrypted_name += alpha_chars[dec_i]
    return decrypted_name

test_input = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]"
]

print get_sector_sum(test_input)

with open('day4.input', 'rt') as f:
    raw_input = f.readlines()

print get_sector_sum(raw_input)

print get_decrypted_name(("qzmt-zixmtkozy-ivhz", 343, ""))

for i in raw_input:
    dec_name = get_decrypted_name(parse_room(i))
    if 'north' in dec_name:
        print dec_name
        print i

