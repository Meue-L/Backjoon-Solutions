import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(sys.stdin.readline().rstrip())
way = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

way.sort()
gcdVal = way[1] - way[0]

for i in range(2, n):
    gcdVal = gcd(gcdVal, way[i] - way[i - 1])

missingCount = (way[-1] - way[0]) // gcdVal - (n - 1)

sys.stdout.write(str(missingCount))
