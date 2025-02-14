import sys

n = int(sys.stdin.readline().rstrip())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
            
    print(int(a*b/gcd(a,b)))