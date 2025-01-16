# Input: Two matrices A and B
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
    for i in range(len(A))
]
print("The resultant matrix after multiplication is:")
for row in result:
    print(row)
