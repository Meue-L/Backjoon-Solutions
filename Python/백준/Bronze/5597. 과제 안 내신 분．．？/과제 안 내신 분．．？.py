import sys

l = [0] * 30

for i in range(28):
    n = int(sys.stdin.readline().rstrip())
    l[n - 1] = 1

for j in range(30):
    if l[j] == 0:
        print(j + 1)
