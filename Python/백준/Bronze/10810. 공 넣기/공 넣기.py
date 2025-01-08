import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

l = [0] * n

for x in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split(" "))
    for y in range(i - 1, j):
        l[y] = k

st = ""
for a in range(len(l)):
    st += str(l[a]) + " "

print(st)
