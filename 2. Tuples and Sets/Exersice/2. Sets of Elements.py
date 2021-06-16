n = int(input())
guests_set = set()
guests = set()

for _ in range(n):
    guests_set.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    else:
        guests.add(guest)

miss_guests = sorted(guests_set.difference(guests))

print(len(miss_guests))
for el in miss_guests:
    print(el)