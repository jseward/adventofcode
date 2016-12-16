def next_data(data):
    a = data
    b = "".join(('1' if (c == '0') else '0') for c in data[::-1])
    return "".join((a, '0', b))

assert next_data('1') == '100'
assert next_data('0') == '001'
assert next_data('11111') == '11111000000'
assert next_data('111100001010') == '1111000010100101011110000'

def fill_data(data, size):
    while len(data) < size:
        data = next_data(data)
    return data

def checksum_char_iter(data):
    i = 0
    while i <= (len(data) - 2):
        yield '1' if data[i] == data[i+1] else '0'
        i += 2

def make_checksum_once(data):
    return [c for c in checksum_char_iter(data)]

def make_checksum(data):
    checksum = [c for c in data]
    while True:
        checksum = make_checksum_once(checksum)
        if len(checksum) % 2 == 1:
            return ''.join(checksum)

assert make_checksum('110010110100') == '100'

data = fill_data('10010000000110000', 272)
checksum = make_checksum(data[0:272])
print checksum

data = fill_data('10010000000110000', 35651584)
checksum = make_checksum(data[0:35651584])
print checksum
