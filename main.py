from collections import defaultdict

n = int(input())
students = {name: grade for _ in range(n) for name, grade in [input().split()]}
grades = defaultdict(list)

for name, grade in students.items():
    grades[grade].append(name)

for grade, name in grades.items():
    print(f'{grade}: {", ".join(name)}')
