# second highest in an array

n = int(input())
arr = map(int, input().split())
    
first=float('-inf')
second=float('-inf')
for i in arr:
  if i>first:
    second=first
    first=i
  elif i>second and i!=first:
    second=i
print(second)
