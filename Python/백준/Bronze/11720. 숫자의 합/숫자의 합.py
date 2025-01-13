import sys

length = int(sys.stdin.readline().rstrip().strip())

N = sys.stdin.readline().rstrip().strip()

count = 0

for i in range(length):
    count += int(N[i])

print(count)
