command = input()
numbers = list(map(int, input().split()))

if command == 'Odd':
    print(sum(filter(lambda x: x % 2 != 0, numbers)) * len(numbers))
else:
    print(sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers))
