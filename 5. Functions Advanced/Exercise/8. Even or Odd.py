def even_odd(*numbers):
    if numbers[-1] == 'odd':
        return list(filter(lambda x: x % 2 != 0, numbers[:-1]))
    else:
        return list(filter(lambda x: x % 2 == 0, numbers[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
