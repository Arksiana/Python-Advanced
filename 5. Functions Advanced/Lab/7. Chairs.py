# РЕКУРСИЯЯ КОМБИНАЦИЯ

def calc_combinations(names_, n_, combs=[]):
    if len(combs) == n_:
        print(*combs, sep=', ')
        return

    for i in range(len(names_)):
        name = names_[i]
        combs.append(name)
        calc_combinations(names_[i + 1:], n_, combs)
        combs.pop()


names = input().split(', ')
n = int(input())
calc_combinations(names, n)