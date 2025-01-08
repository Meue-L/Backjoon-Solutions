import sys

n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split(" ")))

m = max(l)
total = 0

for score in l:
    total += score / m * 100

print(total / n)
