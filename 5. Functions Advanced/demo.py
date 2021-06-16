items = input().split(', ')

data = input()
while not data == "Craft!":
    command, item = data.split(' - ')

    if command == 'Collect':
        if item not in items:
            items.append(item)
    elif command == 'Drop':
        if item in items:
            items.remove(item)
    elif command == 'Combine Items':
        old, new = item.split(':')
        if old in items:
            items.insert(items.index(old) + 1, new)
    elif command == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)

    data = input()

print(*items, sep=', ')
