
from collections import deque

T = int(input())

for i in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    last = float('inf')

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > last:
            print("No")
            break

        last = current

    else:
        print("Yes")
