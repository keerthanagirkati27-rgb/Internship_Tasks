# print unique countries in given size


n = int(input())
a = set()

for i in range(n):
    country = input()
    a.add(country)

print(len(a))
