file = open('even_lines.txt', 'r')
count = 0
new_file = open('line_numbers.txt', 'a')
for line in file:
    count += 1
    letters = 0
    symbols = 0
    text = ''
    for char in line:
        if char.isalnum():
            letters += 1
        elif not char.isalnum() and not char == ' ':
            symbols += 1
    new_file.write(f"Line {count}: {line[:-1]} ({letters})({symbols})\n")
new_file.close()

for line in open('line_numbers.txt', 'r'):
    print(line, end='')
