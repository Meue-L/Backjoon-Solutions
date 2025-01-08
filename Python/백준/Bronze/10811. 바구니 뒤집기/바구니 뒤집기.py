import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
l = [num + 1 for num in range(n)]

for k in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    reversedList = l[: i - 1] + l[i - 1 : j][::-1] + l[j::]
    l = reversedList

print(" ".join(str(num) for num in l))
