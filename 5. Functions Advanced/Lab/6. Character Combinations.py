# 100/100
# from itertools import permutations
# chars = input()
# print(*[f"{''.join(el)}" for el in list(permutations(chars, len(chars)))], sep='\n')

def permute(text, current_index=0):
    if current_index == len(text):
        print(''.join(text))

    for i in range(current_index, len(text)):
        text[current_index], text[i] = text[i], text[current_index]
        permute(text, current_index + 1)
        text[current_index], text[i] = text[i], text[current_index]


string = list(input())
permute(string)
