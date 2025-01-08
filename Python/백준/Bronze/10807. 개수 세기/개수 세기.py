import sys

N = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split(" ")))
v = int(sys.stdin.readline().rstrip())

count = 0

for i in range(N):
    if l[i] == v:
        count += 1

print(count)
