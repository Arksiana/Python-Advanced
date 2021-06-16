def numbers_searching(*args):
    numbers = sorted(list(args))
    duplicates = list(set([x for x in numbers if numbers.count(x) > 1]))
    non_duplicates = list(set(numbers))
    missing = 0

    for el in range(min(non_duplicates), max(non_duplicates)):
        if el not in numbers:
            missing = el
    return [missing, sorted(duplicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))