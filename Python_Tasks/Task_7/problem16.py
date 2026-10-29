def caesarCipher(s, k):
    result = ""

    for ch in s:
        if ch.isalpha():
            if ch.islower():
                result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            else:
                result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            result += ch

    return result
