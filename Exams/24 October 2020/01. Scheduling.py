from collections import deque

jobs = deque(list(map(int, input().split(', '))))
index_of_the_job = int(input())

clock_cycles = 0

# while jobs or min(jobs):
#     current = jobs.popleft()
#     if current == min(jobs):
#         clock_cycles += min(jobs)
#     else:
#         jobs.append(current)


for el in jobs:
    if el <= jobs[index_of_the_job]:
        clock_cycles += el


print(clock_cycles)