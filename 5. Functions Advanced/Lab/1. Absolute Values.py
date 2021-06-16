# def convert_iterable_to_absolute(nums):
#     return [abs(num) for num in nums]
#
#
# numbers = list(map(float, input().split()))
# print(convert_iterable_to_absolute(numbers))


def convert_iterable_to_absolute(nums):
    return list(map(abs, nums))


numbers = list(map(float, input().split()))
print(convert_iterable_to_absolute(numbers))

