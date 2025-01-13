import sys

S = sys.stdin.readline().rstrip()
alphabet = [-1] * 26

for i in range(len(S) - 1, -1, -1):
    # ord("a") = 97
    # ord("z") = 122
    alphabet[ord(S[i]) - 97] = i

print(" ".join(str(index) for index in alphabet))
