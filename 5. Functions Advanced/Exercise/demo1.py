energy = int(input())
command = input()

win_battles = 0
while not command == "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        win_battles += 1
        if win_battles % 3 == 0:
            energy += win_battles
    else:
        print(f"Not enough energy! Game ends with {win_battles} won battles and {energy} energy")
        break

    command = input()

if command == "End of battle":
    print(f"Won battles: {win_battles}. Energy left: {energy}")