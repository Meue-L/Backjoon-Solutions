import sys

l = [0] * 42
count = 0

for i in range(10):
    n = int(sys.stdin.readline().rstrip())
    if l[n % 42] == 0:
        l[n % 42] += 1
        count += 1
    else:
        continue

print(count)
