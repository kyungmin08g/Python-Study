# [ with문 ]
# with 문은 어떤 자원을 사용하기 전에 준비하고, 사용이 끝나면 반드시 정리하는 흐름을 자동화해줍니다.
# 
# Context Manager를 배운 이유는 with문은 Context Manager랑 관련이 있기 때문입니다.
# Context Manager가 관리자라면, with는 그 관리자를 사용하기 위한 문법입니다. with 문 -> Context Manage -> Context
# 정확히는 with문은 Context Manager를 이용해서 어떤 작업의 시작과 종료를 자동으로 관리해주는 문법이죠.

# { 가장 대표적인 예 } - 파일(File)
file = open("../../test/files/hello.txt", "r")

try:
    data = file.read()
    print(data)
finally: # read() 중간에 예외가 발생하면 무조건 파일이 닫히도록 finally문을 직접 써줘야했었습니다.
    file.close()

# 위 try-finally문을 with으로 재구현하였습니다. (try-except-finally문을 간결하고 쉽게 만든 문법이 with문입니다.)
with open("../../test/files/hello.txt", "r") as file: # as value에는 Context Manager의 __enter__() 매직 메소드의 반환 값이 들어갑니다.
    data = file.read()
    print(data)
# 흐름: Context Manager 획득 -> __enter__() -> 반환값(value) -> 작업 실행 -> __exit__() -> 정리/예외 처리
# 즉, with문은 __enter__()와 __exit__()를 자동으로 호출해서 Context의 진입과 종료를 안전하게 관리해주는 문법이라고 이해하면 됩니다.
# 
# with문이 Context Manager를 만드는 게 아니라, 이미 존재하는 Context Manager를 with문으로 사용하는 것입니다. (헷갈리니 조심)
# open() 함수로 예를 들자면 open() -> 파일 객체 반환 -> 파일 객체가 Context Manager 역할 -> with가 __enter__ / __exit__ 사용순으로 동작합니다.
