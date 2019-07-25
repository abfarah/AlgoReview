#Only for use in Python 2.6.0a2 and later
from __future__ import print_function

def karpRabin(s, t):
    h1 = hash(s)
    j = 0
    count = 0
    matches = []
    for i in range(len(s), len(t)+1):
        h2 = hash(t[j:i])
        if h1 == h2:
            if t[j:i] == s:
                count += 1
                matches.append([j,i])
        j+=1
    if count == 0:
        return "No matches found"
    else:
        return str(count) + " matches found at indexes below" + str(matches)

