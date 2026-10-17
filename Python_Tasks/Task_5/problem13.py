n = int(input())
students = []

for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = []

for i in students:
    grades.append(i[1])

grades = sorted(set(grades))
second = grades[1]

names = []

for i in students:
    if i[1] == second:
        names.append(i[0])

for name in sorted(names):
    print(name)
