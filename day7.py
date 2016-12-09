import re

def has_abba(s):
    for i in xrange(len(s)):
        if (i + 3) < len(s):
            if (
                (s[i] != s[i + 1]) and
                (s[i + 1] == s[i + 2]) and
                (s[i] == s[i + 3])
            ):
                return True
    return False 

def supports_tls(ip):
    parts = re.findall(r"[\w]+", ip)
    for i in xrange(len(parts)):
        if i % 2 == 1:
            if has_abba(parts[i]):
                return False 
    for i in xrange(len(parts)):
        if i % 2 == 0:
            if has_abba(parts[i]):
                return True
    return False

def get_aba_blocks(s):
    aba_blocks = []
    for i in xrange(len(s)):
        if (i + 2) < len(s):
            if (
                (s[i] == s[i + 2]) and
                (s[i] != s[i + 1])
            ):
                aba_blocks.append(s[i:i+2])
    return aba_blocks      

def supports_ssl(ip):
    parts = re.findall(r"[\w]+", ip)
    aba_blocks = []
    for i in xrange(len(parts)):
        if i % 2 == 0:
            aba_blocks.extend(get_aba_blocks(parts[i]))
    for i in xrange(len(parts)):
        if i % 2 == 1:
            for aba in aba_blocks:
                bab = aba[1] + aba[0] + aba[1]
                if bab in parts[i]:
                    return True 
    return False


print supports_ssl("aba[bab]xyz")
print supports_ssl("xyx[xyx]xyx")
print supports_ssl("aaa[kek]eke")
print supports_ssl("zazbz[bzb]cdb")

with open('day7.input', 'rt') as f:
    raw_input = f.readlines()

print sum(supports_ssl(ip) for ip in raw_input)




