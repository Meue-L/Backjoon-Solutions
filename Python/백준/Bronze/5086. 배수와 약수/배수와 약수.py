import sys

while True:
    a, b = sys.stdin.readline().rstrip().split(" ")
    a = int(a)
    b = int(b)
    if a == 0 & b == 0:
        break
    
    if b % a == 0:
        print("factor")
    elif a% b == 0:
        print("multiple")
    else:
        print("neither")