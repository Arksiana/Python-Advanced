guests = set()
attended = set()
for _ in range(int(input())):
    num = input()
    guests.add(num)

while True:
    command = input()
    if command == 'END':
        break

    attended.add(input())

unattended = guests - attended
print(len(unattended))
print('\n'.join(sorted(unattended)))