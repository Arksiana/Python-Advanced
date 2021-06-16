from collections import deque

food = int(input())

queue = deque([int(el) for el in input().split()])
biggest_order = max(queue)
print(biggest_order)
while queue:
    current_order = queue.popleft()

    if food >= current_order:
        food -= current_order
    else:
        queue.appendleft(current_order)
        print(f"Orders left: {' '.join(list(map(str, queue)))}")
        break

if not queue:
    print(f"Orders complete")
