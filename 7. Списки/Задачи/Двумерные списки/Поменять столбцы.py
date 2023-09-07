"""
def swap_columns(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)[i]):
            matrix[i][j] = matrix[j][i]
    return matrix


n, m = list(map(int, input().split()))
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
i, j = list(map(int, input().split()))
if swap_columns:
    print(matrix)
"""

def swap_columns(A, i, j):
    for b in range(len(A)):
        A[b][i], A[b][j] = A[b][j], A[b][i]


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=" ")
        print()


n, m = list(map(int, input().split()))
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)
i, j = list(map(int, input().split()))
swap_columns(A, i, j)
print_matrix(A)



