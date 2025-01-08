import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
l = []

for a in range(n):
    l.append(a + 1)

for b in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    temp = l[i - 1]
    l[i - 1] = l[j - 1]
    l[j - 1] = temp

print(" ".join(str(num) for num in l))
