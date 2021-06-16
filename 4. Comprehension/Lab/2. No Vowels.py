word = input()
vowels = {'a', 'o', 'u', 'e', 'i'}
print(''.join([el for el in word if el.lower() not in vowels]))