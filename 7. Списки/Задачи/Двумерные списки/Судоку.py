"""
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
"""

matrix = []
n = int(input())
for i in range(n ** 2):
    row = list(map(int, input().split()))
    matrix.append(row)
    for row in matrix:
        if len(row) == n ** 2:
            if row == [1, n ** 2]:
                print("CORRECT")
            else:
                print("Incorrect")
