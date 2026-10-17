sizem=int(input())
m=set(map(int,input().split()))
sizen=int(input())
n=set(map(int,input().split()))

new=m.symmetric_difference(n)
l=list(new)
b=sorted(l)

for i in b:
    print(i)
