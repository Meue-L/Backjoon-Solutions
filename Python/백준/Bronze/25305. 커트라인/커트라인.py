import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))

nList = list(map(int, sys.stdin.readline().rstrip().split(" ")))

print(sorted(nList)[n-k])