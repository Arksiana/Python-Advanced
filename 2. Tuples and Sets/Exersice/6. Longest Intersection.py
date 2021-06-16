longest_intersection = set()
best_length = 0
for _ in range(int(input())):
    tokens = input().split('-')
    first = tokens[0].split(',')
    second = tokens[1].split(',')

    first_start = int(first[0])
    first_end = int(first[1])

    second_start = int(second[0])
    second_end = int(second[1])

    first_set = set([el for el in range(first_start, first_end + 1)])
    second_set = set([el for el in range(second_start, second_end + 1)])

    intersection = first_set & second_set

    if len(intersection) > best_length:
        best_length = len(intersection)
        longest_intersection = intersection

print(f'Longest intersection is [{", ".join(list(map(str, longest_intersection)))}] with length {best_length}')
