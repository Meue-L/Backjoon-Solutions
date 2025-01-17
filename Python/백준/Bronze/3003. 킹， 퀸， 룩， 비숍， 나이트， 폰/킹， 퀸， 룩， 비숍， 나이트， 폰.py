import sys

pieces = sys.stdin.readline().rstrip().strip().split(" ")

pieces[0] = 1 - int(pieces[0])
pieces[1] = 1 - int(pieces[1])
pieces[2] = 2 - int(pieces[2])
pieces[3] = 2 - int(pieces[3])
pieces[4] = 2 - int(pieces[4])
pieces[5] = 8 - int(pieces[5])

print(" ".join(str(piece) for piece in pieces))
