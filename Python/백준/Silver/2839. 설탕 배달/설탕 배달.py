import sys

n = int(sys.stdin.readline().rstrip())
k = n // 5
count = 0

while True:
    if (n-(k*5))%3 ==0:
        count = k + ((n-(k*5))//3)
        print(count)
        break
    else:
        k -= 1
        
    if k == -1:
        print(-1)
        break