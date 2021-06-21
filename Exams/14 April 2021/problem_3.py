def flights(*args):
    dic = {}
    data = args
    if 'Finish' in data:
        cut = data.index('Finish')
        data = data[0: cut]

    for el in data:
        if type(el) == int:
            index = data.index(el)
            dic[data[index - 1]] += el
        else:
            if el not in dic:
                dic[el] = 0

    return dic


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))