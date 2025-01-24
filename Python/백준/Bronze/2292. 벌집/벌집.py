import sys

n = int(sys.stdin.readline().rstrip())

k = 1
i = 1

while True:
    if n == 1:
        break
    k += 3 + 3*((i*2)-1)
    i+=1
    if n <= k:
        break
print(i)