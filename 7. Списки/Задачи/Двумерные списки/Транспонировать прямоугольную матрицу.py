def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=" ")
        print()


n, m = list(map(int, input().split()))
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
matrix_2 = []
for i in range(len(matrix[0])):
    tmp = []
    for j in range(len(matrix)):
        tmp.append(matrix[j][i])
    matrix_2.append(tmp)
print_matrix(matrix_2)
