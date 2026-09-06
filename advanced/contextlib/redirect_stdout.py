# [ redirect_stdout ]
# print()가 출력하는 장소를 임시로 바꾸는 도구입니다. 조금 특이한 Context Manager입니다. ㅎㅎ

print("Hello") # Hello (일반적으로 터미널에서 출력됩니다.)

from contextlib import redirect_stdout

# { 파일 }
# with 블록 내부의 print()가 그 어딘가로 출력됩니다.
with open("../../test/files/hello.txt", "w") as f:
    with redirect_stdout(f):
        print("Hello")
        print("World")
# 이렇게 코드를 구성할 시 hello.txt 파일에 Hello World가 작성됩니다. 즉, print()문을 파일에다가 작성하게 한 것입니다.
# print() -> sys.stdout -> redirect_stdout -> output.txt
# 평소에는 print("Hello")문으로 터미널에 Hello가 나왔다면, redirect_stdout를 사용했을 떄는 터미널이 아닌 다른 곳에 나오게 된다는 것입니다. (위 코드에서는 파일이죠.)

# { 문자열 }
from io import StringIO

buffer = StringIO()

with redirect_stdout(buffer):
    print("Hello")
    print("World")

result = buffer.getvalue()
print(result) # Hello World
# 즉, 원래 화면에 출력될 내용을 문자열로 가로챌 수 있습니다.

# [ 최종 정리 ]
# print()가 출력하는 장소를 임시로 바꾸는 도구 ((원래 print -> 터미널) -> print -> 터미널 X, 다른 곳 O)
# 들어갈 때: sys.stdout → f로 바꾸고,
# 나올 때: sys.stdout → 원래 stdout으로 복구하는 방식입니다.
