import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split(" "))

print(min(w - x, h - y, x, y))
