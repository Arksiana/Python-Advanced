from collections import deque

litter_in_dispenser = int(input())
people = deque()

while True:
    command = input()
    if command == 'Start':
        break
    else:
        name = command
        people.append(name)

while True:
    command = input()
    if command.isnumeric() and len(people) > 0:
        liters_to_drink = int(command)
        person = people.popleft()
        if liters_to_drink <= litter_in_dispenser:
            print(f"{person} got water")
            litter_in_dispenser -= liters_to_drink
        else:
            print(f"{person} must wait")
    elif command.startswith('refill '):
        liters_to_add = int(command.split(' ')[-1])
        litter_in_dispenser += liters_to_add
    elif command == 'End':
        break
print(f"{litter_in_dispenser} liters left")