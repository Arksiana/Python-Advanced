from collections import deque

customers = deque(list(map(int, input().split(", "))))
taxis = list(map(int, input().split(", ")))

# value of all customers
total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    print(
        f"Not all customers were driven to their destinations\nCustomers left: {', '.join(list(map(str, customers)))}")
