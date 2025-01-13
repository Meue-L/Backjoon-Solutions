import sys

word = sys.stdin.readline().rstrip().upper()
time = 0

for i in range(len(word)):
    x = word[i]
    if x == "A" or x == "B" or x == "C":
        time += 3
    if x == "D" or x == "E" or x == "F":
        time += 4
    if x == "G" or x == "H" or x == "I":
        time += 5
    if x == "J" or x == "K" or x == "L":
        time += 6
    if x == "M" or x == "N" or x == "O":
        time += 7
    if x == "P" or x == "Q" or x == "R" or x == "S":
        time += 8
    if x == "T" or x == "U" or x == "V":
        time += 9
    if x == "W" or x == "X" or x == "Y" or x == "Z":
        time += 10

print(time)
