import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

A = [[0] * m] * n
B = [[0] * m] * n
C = [[0] * m] * n

for i in range(n):
    A[i] = sys.stdin.readline().rstrip().split(" ")
for i in range(n):
    B[i] = sys.stdin.readline().rstrip().split(" ")

for i in range(n):
    for j in range(m):
        C[i][j] = int(A[i][j]) + int(B[i][j])
    print(" ".join(str(CComponent) for CComponent in C[i]))
