n = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(n)]
result = [[el for el in col if el % 2 == 0] for col in matrix]
print(result)
