class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        super().__init__(f"{value} is negative")


def validate_positive_numbers(numbers_):
    for number in numbers_:
        if number < 0:
            raise ValueCannotBeNegativeError(number)


numbers = [1, 2, 3, 4, 5, -3]
validate_positive_numbers(numbers)
print("Numbers are positive")
