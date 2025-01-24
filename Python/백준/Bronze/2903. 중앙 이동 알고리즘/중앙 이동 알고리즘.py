import sys

n = int(sys.stdin.readline().rstrip())

k = 2

for i in range(n):
    k = (k+(k-1))
    
print(k ** 2)