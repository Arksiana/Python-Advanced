def update_heroes(name, item, cost, heroes):
    if not heroes[name].get(item):
        heroes[name].update({item: cost})
    return heroes


names = input().split(', ')
heroes = {name: {} for name in names}

command = input()

while not command == 'End':
    name, item, cost = command.split('-')
    cost = int(cost)
    heroes = update_heroes(name, item, cost, heroes)

    command = input()

print(*[f'{name} -> Items: {len(items)}, Cost: {sum([items[price] for price in items])}' for name, items in
        heroes.items()], sep='\n')
