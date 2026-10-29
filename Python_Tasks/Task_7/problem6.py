
def pangrams(s):
    if len(set(s.lower().replace(" ", ""))) == 26:
        return "pangram"
    else:
        return "not pangram"
