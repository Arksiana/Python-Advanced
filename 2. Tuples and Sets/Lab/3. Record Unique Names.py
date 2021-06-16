# names = set()
# for _ in range(int(input())):
#     name = input()
#     if name not in names:
#         print(name)
#         names.add(name)

# ONE LINE
print('\n'.join(set((input() for _ in range(int(input()))))))
