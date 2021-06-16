numbers_tuple = tuple(map(float, input().split()))

numbers_occure = {}

for num in numbers_tuple:
    if num not in numbers_occure:
        numbers_occure[num] = 0
    numbers_occure[num] += 1

[print(f'{key} - {value} times') for key, value in numbers_occure.items()]