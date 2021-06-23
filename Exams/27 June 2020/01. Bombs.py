from collections import deque

effects = deque(list(map(int, input().split(', '))))
casting = list(map(int, input().split(', ')))
is_fill = False

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

bombs_count = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while effects and casting:
    if all(x >= 3 for x in bombs_count.values()):
        break
    first_effect = effects[0]
    last_cast = casting[-1]

    current_sum = first_effect + last_cast

    if current_sum in bombs:
        current = bombs[first_effect + last_cast]
        bombs_count[current] += 1
        effects.popleft()

        casting.pop()
    else:
        casting[-1] -= 5

if all(x >= 3 for x in bombs_count.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(list(map(str,effects)))}" if effects else "Bomb Effects: empty")
print(f"Bomb Casings: {', '.join(list(map(str,casting)))}" if casting else "Bomb Casings: empty")
for k, v in sorted(bombs_count.items(), key=lambda x: x):
    print(f"{k}: {v}")
# print(f"{k}: {v}" for k, v in sorted(bombs_count.items(), key=lambda x: x))
