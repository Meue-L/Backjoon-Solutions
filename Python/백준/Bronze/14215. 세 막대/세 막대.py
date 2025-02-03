import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))

if max(a, b, c) >= (a + b + c - max(a, b, c)):
    print((2 * (a + b + c)) - (2 * max(a, b, c)) - 1)
else:
    print(a + b + c)
