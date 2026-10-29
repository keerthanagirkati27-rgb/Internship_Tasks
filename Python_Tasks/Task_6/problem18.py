n = int(input())
a = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command, length = input().split()
    b = set(map(int, input().split()))

    if command == "intersection_update":
        a.intersection_update(b)
    elif command == "update":
        a.update(b)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    elif command == "difference_update":
        a.difference_update(b)

print(sum(a))
