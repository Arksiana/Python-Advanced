# def sums(a, b):
#     return a + b
#
#
# def calculate_a_plus_b(a, b):
#     return sums(a, b)
#
#
# print(calculate_a_plus_b(1, 2))


class Stack:
    def __init__(self, items):
        self.__items = []

    def pop(self):
        return self.__items.pop()

    def append(self, item):
        self.__items.append(item)

    def size(self):
        return len(self.__items)


stack = Stack(list(input()))

while stack.size() > 0:
    item = stack.pop()
    print(item, end="")
print("")
