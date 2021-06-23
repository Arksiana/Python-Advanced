def list_manipulator(numbers, com_1, com_2, *args):
    if com_1 == 'add' and com_2 == 'beginning':
        nums = list(args)
        numbers = nums + numbers

    elif com_1 == 'add' and com_2 == 'end':
        nums = args
        for el in nums:
            numbers.append(el)

    elif com_1 == 'remove' and com_2 == 'beginning':
        if args:
            numbers = numbers[int(*args):]
        else:
            numbers.remove(numbers[0])

    elif com_1 == 'remove' and com_2 == 'end':
        if args:
            [numbers.pop() for _ in range(int(*args))]
        else:
            numbers.pop()

    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))

print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
