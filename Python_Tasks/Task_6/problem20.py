n = int(input())

for _ in range(n):
    s = input()

    if len(s) == 10 and s.isdigit() and s[0] in "789":
        print("YES")
    else:
        print("NO")
