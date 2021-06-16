from collections import deque

green_time = int(input())
window_time = int(input())
all_cars = []
cars = deque()
crashed = False
line = input()
while not line == 'END':
    if line == 'green':
        green_timer = green_time
        if cars:
            copy = cars.popleft()
            current = deque(copy)
            while green_timer:
                if not current:
                    if cars:
                        copy = cars.popleft()
                        current = deque(copy)
                    else:
                        break
                current.popleft()
                green_timer -= 1
            if current:
                window_timer = window_time
                while window_timer and current:
                    current.popleft()
                    window_timer -= 1
            if current:
                crashed = True
                print('A crash happened!')
                print(f'{copy} was hit at {current.popleft()}.')
                break
    else:
        cars.append(line)
        all_cars.append(line)

    line = input()

if not crashed:
    print(f"Everyone is safe.")
    print(f"{len(all_cars) - len(cars)} total cars passed the crossroads.")