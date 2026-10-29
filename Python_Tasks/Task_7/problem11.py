
def twoStrings(s1, s2):
    for ch in s2:
        if ch in s1:
            return "YES"
    return "NO"
