import sys

while True:
    try:
        line = sys.stdin.readline().rstrip()
        if line == "":
            # readline의 경우 입력값이 없을경우 EOF에러가 발생되지 않는다.
            # 단순히 빈 문자열을 반환. 따라서 예외처리를 따로 해주어야 한다.
            raise EOFError
        print(line)
    except EOFError:
        # 입력값이 없으면 예외처리.(EOFerror)
        break
