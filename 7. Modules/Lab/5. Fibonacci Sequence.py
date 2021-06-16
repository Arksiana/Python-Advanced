from fibb_seq import *


seq = []
while True:
    command = input()

    if command == 'Stop':
        break

    if command.split()[0] == 'Create':
        count = int(command.split()[-1])
        seq = fibonacci_seq(count)
        print(" ".join(list(map(str, seq))))

    elif command.split()[0] == 'Locate':
        number = int(command.split()[-1])
        print(fibonacci_locate(seq, number))