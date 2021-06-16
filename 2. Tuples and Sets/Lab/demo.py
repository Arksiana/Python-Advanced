from copy import deepcopy

l = [{'a': 2}]
l2 = deepcopy(l)

print(l)
print(id(l))
print(l2)
print(id(l2))

l2[0]['b'] = 3

print(l)
print(id(l))
print(l2)
print(id(l2))
