import sys

word = list(sys.stdin.readline().rstrip().upper())
spellList = [0] * 26
maxValue = 0
maxIndex = -1

for spell in word:
    spellList[int(ord(spell)) - 65] += 1

for i in range(len(spellList)):
    if spellList[i] != 0:
        if spellList[i] > maxValue:
            maxIndex = i
            maxValue = spellList[i]
        elif spellList[i] == maxValue:
            maxIndex = -2

print(chr(maxIndex + 65))
