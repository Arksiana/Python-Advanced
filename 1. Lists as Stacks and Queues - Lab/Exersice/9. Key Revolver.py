from collections import deque

price_bullet = int(input())
barrel = int(input())
bullet_stack = list(map(int, input().split(' ')))
lock_queue = deque(list(map(int, input().split(' '))))
intelligence = int(input())
count = 0

while lock_queue:
    if not bullet_stack:
        print(f"Couldn't get through. Locks left: {len(lock_queue)}")
        quit()

    while bullet_stack and lock_queue:
        count += 1
        current_bullet = bullet_stack.pop()
        if lock_queue[0] >= current_bullet:
            lock_queue.popleft()
            print(f'Bang!')
        else:
            print(f'Ping!')

        if bullet_stack and count%barrel==0:
            print(f'Reloading!')

print(f'{len(bullet_stack)} bullets left. Earned ${intelligence - (count * price_bullet)}')