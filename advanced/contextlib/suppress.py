# [ suppress ]
# suppress는 특정 예외를 발생해도 무시하고 넘어가게 하는 Context Manager입니다.

from contextlib import suppress

class OS:
    def remove(self, s: str) -> None:
        print("삭제")

os = OS()

# try-except문으로 작성
try:
    os.remove("test.txt")
except FileNotFoundError:
    pass

# with suppress 사용할 때
# 위 try-except문으로 작성된 코드를 with문으로 바꾸면 다음과 같이 바꿀 수 있습니다.
with suppress(FileNotFoundError):
    os.remove("test.txt")
# 파일이 존재하지 않을 때
# 내부 동작은 os.remove() -> FileNotFoundError 발생 -> suppress가 해당 예외를 확인 -> 예외를 전파하지 않음 -> 프로그램 계속 실행 순으로 진행됩니다.
# 
# 위 코드를 봤을 때 try-except문으로 작성한 코드가 이렇게 확 줄어든 것을 볼 수 있습니다.
# 중요한 점은 suppress는 모든 예외를 무시하는 게 아닙니다. 위 코드와 같이 특정 예외만 무시하고 넘어갑니다.

# { 언제 사용할까요? }
# 대표적으로 없어도 상관없는 작업에 사용합니다.
with suppress(FileNotFoundError): # temp.txt가 있으면 삭제하고, 없으면 그냥 넘어가라는 의미의 코드입니다.
    os.remove("temp.txt")
# 즉, suppress = 특정 예외를 의도적으로 무시
