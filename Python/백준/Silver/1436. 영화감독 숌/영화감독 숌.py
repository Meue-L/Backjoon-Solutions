import sys

n = int(sys.stdin.readline().rstrip())
count = 0
num = 665

while True:
    num +=1
    for i in range(len(str(num))):
        if str(num)[i:i+3] == "666":
            count +=1
            break
        
    if count == n:
        print(num)
        break