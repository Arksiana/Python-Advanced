import os


def create_file(name):
    file = open(name, 'w')
    file.close()


def add_in_file(name, text):
    file = open(name, 'a')
    file.write(text)
    file.write('\n')
    file.close()


def replace_file(name, old, new):
    lines = open(name, 'r')
    file_rep = open('file_rep.txt', 'w')
    for line in lines:
        file_rep = open('file_rep.txt', 'a')
        if old in line:
            file_rep.write(line.replace(old, new))
            # file_rep.write('\n')
        else:
            file_rep.write(line)
            # file_rep.write('\n')
        file_rep.close()
    file = open('file.txt', 'w')
    for line in open('file_rep.txt', 'r'):
        file = open('file.txt', 'a')
        file.write(line)
        file.close()


def delete(name):
    os.remove(name)


while True:
    line = input()
    if line == 'End':
        break
    command = line.split('-')
    if command[0] == 'Create':
        file = create_file(command[1])
    elif command[0] == 'Add':
        file = add_in_file(command[1], command[2])
    elif command[0] == 'Replace':
        try:
            file = replace_file(command[1], command[2], command[3])
        except FileNotFoundError:
            print(f'An error occurred')
    elif command[0] == 'Delete':
        try:
            file = delete(command[1])
        except FileNotFoundError:
            print(f'An error occurred')
