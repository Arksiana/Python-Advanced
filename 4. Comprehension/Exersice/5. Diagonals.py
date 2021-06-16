n = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
# matrix = [list(map(int, input(', ').split())) for _ in range(n)]

print(f"First diagonal: {', '.join([str(matrix[i][i]) for i in range(n)])}. Sum: {sum(matrix[i][i] for i in range(n))} ")
print(f"Second diagonal: {', '.join([str(matrix[i][n - i - 1]) for i in range(n)])}. Sum: {sum(matrix[i][n - i - 1] for i in range(n))} ")
