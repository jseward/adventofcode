
import hashlib
import re


STRETCH = 2016
RANGE = 1000


def make_hash(salt, index):
    md5 = hashlib.md5()
    md5.update("{}{}".format(salt, index))
    hash = md5.hexdigest()
    for i in xrange(STRETCH):
        md5_stretch = hashlib.md5()
        md5_stretch.update(hash)
        hash = md5_stretch.hexdigest()
    return hash

def get_first_triplet(hash):
    triplets = re.findall(r"(\w)\1{2,}", hash)
    if triplets:
        return triplets[0]
    return None

def get_all_quintuplets(hash):
    return re.findall(r"(\w)\1{4,}", hash)

def make_keys(salt, num_keys):
    keys = []
    triplets = {}
    quintuplets = {}

    def update(index):
        hash = make_hash(salt, index)
        hash_triplet = get_first_triplet(hash)
        if hash_triplet:
             triplets[index] = hash_triplet
        hash_quintuplets = get_all_quintuplets(hash)
        if hash_quintuplets:
            quintuplets[index] = hash_quintuplets

    for i in xrange(RANGE):
        update(i)

    i = 0
    while len(keys) < num_keys:
        update(RANGE + i)

        if i in triplets:
            for k in xrange(RANGE):
                q = quintuplets.get(i + k + 1, None)
                if q and (triplets[i] in q):
                    keys.append(i)

        i += 1
    
    print keys[num_keys - 1]


#make_keys("abc", 64)
make_keys("qzyelonm", 64)

