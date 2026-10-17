
n = int(input())
students = {}

for i in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    students[name] = marks

query_name = input()

avg = sum(students[query_name]) / len(students[query_name])

print(f"{avg:.2f}")
