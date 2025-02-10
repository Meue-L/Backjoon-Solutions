import sys

n = sys.stdin.readline().rstrip()

print("".join(str(n) for n in (reversed(sorted(n)))))