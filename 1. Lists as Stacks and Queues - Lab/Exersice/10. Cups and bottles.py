from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))
wasted_water = 0
flag = True

while cups:
    if bottles:
        dif = cups[0] - bottles.pop()
        if dif < 0:
            wasted_water += abs(dif)
            cups.popleft()
        elif dif > 0:
            cups[0] = dif
        else:
            cups.popleft()
    else:
        print(f"Cups:", *cups, sep=' ')
        print(f'Wasted litters of water: {wasted_water}')
        flag = False
        break

if flag:
    print(f'Bottles:', *bottles, sep=' ')
    print(f'Wasted litters of water: {wasted_water}')