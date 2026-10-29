
from collections import Counter

def isValid(s):
    freq = Counter(Counter(s).values())
    
    if len(freq) == 1:
        return "YES"
    
    if len(freq) == 2:
        keys = list(freq.keys())
        values = list(freq.values())
        
        if (keys[0] == 1 and values[0] == 1) or (keys[1] == 1 and values[1] == 1):
            return "YES"
        
        if abs(keys[0] - keys[1]) == 1:
            if (keys[0] > keys[1] and values[0] == 1) or (keys[1] > keys[0] and values[1] == 1):
                return "YES"
    
    return "NO"
