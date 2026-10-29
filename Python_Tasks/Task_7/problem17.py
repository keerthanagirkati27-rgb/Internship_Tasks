
def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]
        num = int(first)
        result = first

        while len(result) < len(s):
            num += 1
            result += str(num)

        if result == s:
            print("YES", first)
            return

    print("NO")
