import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
c, d = map(int, sys.stdin.readline().rstrip().split(" "))

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
bottom = b*d

top = bottom/b*a+bottom/d*c

temp = gcd(bottom, top)

print(int(top/temp), int(bottom/temp))