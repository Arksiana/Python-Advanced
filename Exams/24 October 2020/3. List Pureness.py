import collections


def best_list_pureness(*args):
    ll = args[0]
    k = args[1]
    pureness_value = 0
    count_rotations = 0
    nums_dq = collections.deque(ll)
    for n in range(0, k + 1):
        current = sum([el * nums_dq.index(el) for el in nums_dq])
        if current > pureness_value:
            pureness_value = current
            count_rotations = n
        nums_dq.rotate(1)

    return f"Best pureness {pureness_value} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
