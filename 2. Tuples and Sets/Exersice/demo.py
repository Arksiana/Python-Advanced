box = [int(el) for el in input().split()]
capacity = int(input())

racks = 1
current_capacity = capacity

while len(box) > 0:
    current_v_cloth = box.pop()

    if current_v_cloth <= current_capacity:
        current_capacity -= current_v_cloth
    else:
        racks += 1
        current_capacity = capacity
        current_capacity -= current_v_cloth

print(racks)

