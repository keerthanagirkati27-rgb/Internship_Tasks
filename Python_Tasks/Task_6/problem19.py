s = input()

for char in sorted(set(s), key=lambda x: (-s.count(x), x))[:3]:
    print(char, s.count(char))
