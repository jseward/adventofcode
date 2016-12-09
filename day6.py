from collections import defaultdict
import operator

def get_message(codes):
    code_len = len(codes[0])
    char_counts = [defaultdict(int) for i in xrange(code_len)]
    for code in codes:
        assert(len(code) == code_len)
        for i in xrange(code_len):
            char_counts[i][code[i]] += 1
    
    message = ""
    for i in xrange(code_len):
        sorted_chars = sorted(char_counts[i].items(), key=operator.itemgetter(1), reverse=False)
        message += sorted_chars[0][0]

    return message
    

codes = [
"eedadn",
"drvtee",
"eandsr",
"raavrd",
"atevrs",
"tsrnev",
"sdttsa",
"rasrtv",
"nssdts",
"ntnada",
"svetve",
"tesnvt",
"vntsnd",
"vrdear",
"dvrsen",
"enarar"
]

print get_message(codes)

with open('day6.input', 'rt') as f:
    raw_input = f.readlines()

print get_message([i.strip() for i in raw_input])