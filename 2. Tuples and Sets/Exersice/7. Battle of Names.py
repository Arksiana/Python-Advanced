even_set = set()
odd_set = set()
n = int(input())

for i in range(1, n + 1):
    name = input()
    summed = sum([ord(el) for el in name]) // i

    if summed % 2 == 0:
        even_set.add(summed)
    else:
        odd_set.add(summed)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(', '.join(map(str, odd_set.union(even_set))))
elif odd_sum > even_sum:
    print(', '.join(map(str, odd_set.difference(even_set))))
else:
    print(', '.join(map(str, odd_set.symmetric_difference(even_set))))
