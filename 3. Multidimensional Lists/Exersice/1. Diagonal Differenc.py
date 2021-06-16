n = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(n)]
sum_first = sum(matrix[i][i] for i in range(n))
sum_second = sum(matrix[i][n-i-1] for i in range(n))
print(abs(sum_first - sum_second))