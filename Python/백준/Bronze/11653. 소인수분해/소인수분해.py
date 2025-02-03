import sys

n = int(sys.stdin.readline().rstrip())
while True:
    try:
        if n == 1:
            raise EOFError

        for i in range(2, n + 1, 1):
            if n % i == 0:
                print(i)
                n = int(n / i)
                break

    except EOFError:
        break
