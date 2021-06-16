from collections import deque

customers = deque([int(el) for el in input().split(', ')])
taxis = ([int(el) for el in input().split(', ')])
total_time = 0

while customers or taxis:
    c_customer = customers.popleft()
    c_taxi = taxis.pop()

    if c_taxi >= c_customer:
        total_time += c_customer
    else:
        customers.appendleft(c_customer)

    if len(taxis) == 0:
        break

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f'Customers left: {", ".join(list(map(str, customers)))}')