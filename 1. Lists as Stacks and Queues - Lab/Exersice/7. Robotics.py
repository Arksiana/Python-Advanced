from collections import deque


def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return h, m, s


robots = input().split(';')
time = [int(el) for el in input().split(':')]

available_robots = deque()
waiting_robots = deque()
products = deque()
robot_dict = {}

product = input()
while not product == 'End':
    products.append(product)

    product = input()

for robot in robots:
    robot_name, robot_time = robot.split('-')
    robot_time = int(robot_time)
    available_robots.append([robot_name, robot_time])
    robot_dict[robot_name] = robot_time

while products:
    for robot in waiting_robots:
        robot_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([robot_name, robot_dict[robot_name]])
    waiting_robots = [el for el in waiting_robots if el[1] > 0]

    time = next_second(time[0], time[1], time[2])
    current_product = products.popleft()
    if not available_robots:
        products.append(current_product)
        continue
    current_robot = available_robots.popleft()
    print(f"{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")

    waiting_robots.append(current_robot)
