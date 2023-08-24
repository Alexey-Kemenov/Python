matrix = []
max_i = 0
max_j = 0
n, m = list(map(int, input().split()))
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[max_i][max_j]:
            max_i = i
            max_j = j
print(max_i, max_j)
