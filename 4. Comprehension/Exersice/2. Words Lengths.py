text = input().split(', ')
print(', '.join([f'{el} -> {len(el)}' for el in text]))
