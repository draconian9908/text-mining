""" Text Processing
    Lydia Hodges
    Text Similarity Between Contemporary Fiction Novels (1894)"""

#pan_dict = {}
#pem_dict = {}
from math import sqrt

def build_dict(filename):
    di = {}
    fp = open(filename)
    for line in fp:
        for word in line.rstrip().split():
            if word in di:
                di[word] += 1
            else:
                di[word] = 1
    return di

pan_dict = build_dict('pan.txt')
pem_dict = build_dict('pembroke.txt')
jungle_dict = build_dict('jungle.txt')
spitfire_dict = build_dict('spitfire.txt')
death_dict = build_dict('death.txt')
list_dict = [pan_dict, pem_dict, jungle_dict, spitfire_dict, death_dict]

def compare(d1,d2):
    temp = []
    keys1 = set(d1.keys())
    keys2 = set(d2.keys())
    key = keys1.union(keys2)
    for_indexing = list(key)
    num = len(key)
    for i in for_indexing:
        if i not in d2 or i not in d1:
            val = 0
        else:
            val = (d1[i] * d2[i]) / (sqrt(d1[i] ** 2) * sqrt(d2[i] ** 2))
        temp.append(val)
    tot = sum(temp)
    final = tot / num
    return round(final,5)

def build_sim(dicts):
    sims = []
    for i in dicts:
        temp = []
        for j in dicts:
            temp.append(compare(i,j))
        sims.append(str(temp))
    return sims

simularity = build_sim(list_dict)
print('\n'.join(simularity))
