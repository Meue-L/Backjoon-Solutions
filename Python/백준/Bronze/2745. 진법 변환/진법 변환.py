import sys

N, B = sys.stdin.readline().rstrip().split(" ")

sum = 0
count = 0

for i in range(len(N)):
    if N[i] in "1234567890":
        sum += (int(B) ** (len(N) - (i + 1))) * int(N[i])
    else:
        sum += (int(B) ** (len(N) - (i + 1))) * (int(ord(N[i])) - 55)

print(sum)
