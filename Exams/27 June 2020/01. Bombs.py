from collections import deque

bomb_effect = deque(list(map(int, input().split(', '))))
bomb_casings = list(map(int, input().split(', ')))

bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

"""
Bombs:
•	Datura Bombs: 40
•	Cherry Bombs: 60
•	Smoke Decoy Bombs: 120

"""

while bomb_casings and bomb_effect:

    if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
        break

    current_effect = bomb_effect.popleft()
    current_casting = bomb_casings.pop()

    current_sum = current_effect + current_casting

    if current_sum == 40:
        bombs['Datura Bombs'] += 1
    elif current_sum == 60:
        bombs['Cherry Bombs'] += 1
    elif current_sum == 120:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        current_casting -= 5
        bomb_effect.appendleft(current_effect)
        bomb_casings.append(current_casting)

sum_values = sum([v for k, v in bombs.items()])

if sum_values >= 9:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print("Bomb Effects: empty" if not bomb_effect else f"Bomb Effects: " + ', '.join(list(map(str, bomb_effect))))
print("Bomb Casings: empty" if not bomb_casings else f"Bomb Casings: " + ', '.join(list(map(str, bomb_casings))))

for k, v in sorted(bombs.items(), key=lambda x: x):
    print(f"{k}: {v}")
