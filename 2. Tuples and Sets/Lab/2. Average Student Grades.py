from collections import defaultdict

n = int(input())
students = defaultdict(list)

for _ in range(n):
    name, mark = input().split()
    mark = float(mark)
    students[name].append(mark)

for name, marks in students.items():
    mark_str = ' '.join((map(lambda f: format(f, '.2f'), marks)))
    print(f"{name} -> {mark_str} (avg: {(sum(marks) / len(marks)):.2f})")