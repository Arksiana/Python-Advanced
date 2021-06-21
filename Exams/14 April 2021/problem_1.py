from collections import deque

pizza_orders = deque(list(map(int, input().split(', '))))
employee_capacities = list(map(int, input().split(', ')))
total_pizza_orders = 0
completed = True

while pizza_orders:

    pizzas = pizza_orders[0]
    capacity = employee_capacities[-1]

    if pizzas > 10 or pizzas <= 0:
        pizza_orders.popleft()
    elif pizzas <= capacity:
        pizza_orders.popleft()
        employee_capacities.pop()
        total_pizza_orders += pizzas
    elif pizzas > capacity:
        pizza_orders[0] -= capacity
        total_pizza_orders += capacity
        employee_capacities.pop()

    if not employee_capacities:
        completed = False
        print("Not all orders are completed.")
        print(f"Orders left: {', '.join(list(map(str, pizza_orders)))}")
        break

if completed:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_orders}")
    print(f"Employees: {', '.join(list(map(str, employee_capacities)))}")