
def makingAnagrams(s1, s2):
    count = 0

    for ch in set(s1 + s2):
        count += abs(s1.count(ch) - s2.count(ch))

    return count
