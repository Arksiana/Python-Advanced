from collections import deque

people = deque(input().split(' '))
n_toss = int(input())

while len(people) > 1:
    people.rotate(-(n_toss))
    loser = people.pop()
    print(f'Removed {loser}')
winner = people.pop()
print(f"Last is {winner}")