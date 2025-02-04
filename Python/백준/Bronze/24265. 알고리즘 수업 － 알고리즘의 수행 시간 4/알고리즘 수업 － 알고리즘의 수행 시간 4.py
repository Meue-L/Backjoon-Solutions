import sys

n = int(sys.stdin.readline().rstrip())

count = 0

for i in range(n-1):
    count += n - (i+1)
        
print(count)
print(2)
    