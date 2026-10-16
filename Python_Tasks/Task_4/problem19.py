from collections import Counter

n = int(input())
sizes = list(map(int, input().split()))
shoes = Counter(sizes)

customers = int(input())
money = 0

for i in range(customers):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        money += price
        shoes[size] -= 1

print(money)
