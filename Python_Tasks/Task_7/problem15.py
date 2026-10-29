
from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)
    odd = 0

    for count in freq.values():
        if count % 2 != 0:
            odd += 1

    if odd <= 1:
        return "YES"
    else:
        return "NO"
