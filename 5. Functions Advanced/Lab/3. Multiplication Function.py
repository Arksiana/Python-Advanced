from functools import reduce


def multiply(*nums):
    return reduce(lambda x, y: x * y, nums)


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
