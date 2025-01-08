import sys

maxNum = 0
index = -1

for i in range(9):
    n = int(sys.stdin.readline().rstrip())
    if maxNum < n:
        maxNum = n
        index = i + 1

print(maxNum)
print(index)
