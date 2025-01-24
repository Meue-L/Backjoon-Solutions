import sys

N, B = sys.stdin.readline().rstrip().split(" ")
n = int(N)
b = int(B)

decNum = []
i=0
# print(ord("A")) 65

while True:
    i+=1
    
    if n%(b) > 9:
        decNum.append(chr(((n%(b)))+55))
    else:
        decNum.append(n%(b))
        
    n = n//b
    
    if n == 0:
        break
    
    
print("".join(str(letter) for letter in reversed(decNum)))