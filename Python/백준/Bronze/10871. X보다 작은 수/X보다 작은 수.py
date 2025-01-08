import sys

n, x = map(int, sys.stdin.readline().rstrip().split(" "))
l = list(map(int, sys.stdin.readline().rstrip().split(" ")))

l2 = ""
count = 0

for i in range(n):
    if l[i] < x:
        l2 += str(l[i]) + " "

print(l2.strip())
