row, col = list(map(int, input().split()))

matrix = [[f'{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}' for c in range(col)] for r in range(row)]
# for row in matrix:
#     print(' '.join(list(map(str, row))))
#
print("\n".join([" ".join([col for col in row]) for row in matrix]))
