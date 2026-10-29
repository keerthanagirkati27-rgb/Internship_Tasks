
from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    s1 = s[:n//2]
    s2 = s[n//2:]

    c1 = Counter(s1)
    c2 = Counter(s2)

    return sum((c1 - c2).values())
