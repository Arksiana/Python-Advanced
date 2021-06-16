counties = [x for x in input().split(', ')]
cities = [x for x in input().split(', ')]
result = dict(zip(counties, cities))
print('\n'.join(f'{key} -> {value}' for key, value in result.items()))


# for key, value in result.items():
#     print(f'{key} -> {value}')
