import collections

nums = [4, 3, 2, 6]
best = 0
best_rotation = 0
nums_dq = collections.deque(nums)
for n in range(4):
    sums_list = 0
    best_rotation += 1
    sums_list = sum([el * nums_dq.index(el) for el in nums_dq])
    if sums_list > best:
        best = sums_list
        best_rotation = n
    nums_dq.rotate(1)

print(best)
print(best_rotation)