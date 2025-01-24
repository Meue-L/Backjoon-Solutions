import sys

x = int(sys.stdin.readline().rstrip())

i=0

while True:
    i += 1
    if i >= x:
        break
    x -= i

if i % 2 ==1:
    print(f"{i-(x-1)}/{x}")
else:
    print(f"{x}/{i-(x-1)}")