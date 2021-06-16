parking = set()

for _ in range(int(input())):
    direction, car_number = input().split(', ')
    operations = {
        'IN': parking.add,
        'OUT': parking.remove
    }
    operations[direction](car_number)

if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')
