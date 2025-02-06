import sys

n = sys.stdin.readline().rstrip()
if len(n) <= 2:
    num = 0
else:
    num = (10 ** (len(n)-1))* (int(n[0])-1)
    
while True:
    if num + sum(int(k) for k in str(num)) == int(n):
        print(num)
        break
    
    if num == int(n):
        print(0)
        break
    num += 1