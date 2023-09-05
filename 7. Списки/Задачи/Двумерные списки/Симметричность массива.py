def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


matrix = []
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
if is_symmetric(matrix):
    print("YES")
else:
    print("NO")


