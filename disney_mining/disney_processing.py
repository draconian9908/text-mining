""" Disney Processing
    Lydia Hodges
    Text Similarity Between the Original Stories Disney was Inspired By"""

from math import sqrt

def build_dict(filename):
    """ Builds a dictionary for the file.

        key = unique word in text
        value = frequency of wrod in text
    """
    di = {}
    fp = open(filename)
    for line in fp:
        for word in line.rstrip().split():
            if word in di:
                di[word] += 1
            else:
                di[word] = 1
    return di

# Building the dictionaries for each of the text files and putting the dictionaries in a list.
cinderella_dict = build_dict('cinderella.txt')
mermaid_dict = build_dict('mermaid.txt')
beast_dict = build_dict('beast.txt')
sleeping_dict = build_dict('sleeping.txt')
snow_dict = build_dict('snow.txt')
list_dict = [cinderella_dict, mermaid_dict, beast_dict, sleeping_dict, snow_dict]

def compare(d1,d2):
    """ Uses cosine similarity to compare two dictionaries.

        Sets are used to check for all words across both texts.
    """
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
    """ Uses the Compare function to compare all the dictionaries in a list to each other.
    """
    sims = []
    for i in dicts:
        temp = []
        for j in dicts:
            temp.append(compare(i,j))
        sims.append(str(temp))
    return sims

similarity = build_sim(list_dict)
print('\n'.join(similarity)) # Splits the cosine similarities associated with each text on separate lines.
