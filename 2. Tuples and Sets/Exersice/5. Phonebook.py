line = input().split('-')
phonebook = {}

while len(line) != 1:
    name = line[0]
    number = line[1]
    phonebook[name] = number
    line = input().split('-')

for el in range(int(line[0])):
    name = input()

    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
