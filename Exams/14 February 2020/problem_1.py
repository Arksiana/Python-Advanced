from collections import deque

firework_effect = deque(list(map(int, input().split(", "))))
explosive_power = deque(list(map(int, input().split(", "))))

firework_effect = deque([el for el in firework_effect if el > 0])
explosive_power = deque([el for el in explosive_power if el > 0])

palm = 0
willow = 0
crossette = 0
perfect = False


def remove(effect, explosive):
    effect.popleft()
    explosive.pop()
    return effect, explosive


while len(firework_effect) > 0 and len(explosive_power) > 0:

    if firework_effect[0] <= 0:
        firework_effect.popleft()

    if explosive_power[-1] <= 0:
        explosive_power.pop()

    first = firework_effect.popleft()
    last = explosive_power.pop()
    power = first + last

    if power % 3 == 0 and not power % 5 == 0:
        palm += 1
        # remove(firework_effect, explosive_power)

    elif power % 5 == 0 and not power % 3 == 0:
        willow += 1
        # remove(firework_effect, explosive_power)

    elif power % 3 == 0 and power % 5 == 0:
        crossette += 1
        # remove(firework_effect, explosive_power)
    else:
        first -= 1
        if first > 0:
            firework_effect.append(first)
        explosive_power.append(last)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        print("Congrats! You made the perfect firework show!")
        perfect = True
        break

if not perfect:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effect:
    print(f"Firework Effects left: {', '.join(list(map(str, firework_effect)))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(list(map(str, explosive_power)))}")
print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
