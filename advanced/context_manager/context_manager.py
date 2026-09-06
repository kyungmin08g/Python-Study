# [ Context란 무엇인가? ]
# 영어로 Context는 맥락, 상황, 환경이라는 뜻이자만, 프로그래밍에서는 특정 코드가 실행되는 동안 특정한 상태나 환경이 유지되는 상황을 의미하는 경우입니다.
# 파일로 예를 들자면 파일 닫힘 -> 파일 열기 -> 파일이 열린 상태(Context) -> 파일 닫기 -> 파일 닫힘 순으로 플로우가 있습니다. Context는 파일이 열린 상태에서 할 수 있는 것들을 말합니다.
# 
# 1. Context의 핵심은 '상태'입니다.
# 정확히는 어떤 작업을 수행하기 위해 특정한 상태에 들어가 있는 것을 의미합니다.
# ex. 파일(파일이 열린 상태), Lock(Lock을 획득한 상태), DB Transaction(Transaction이 시작된 상태), 네트워크(Connection이 열린 상태) 등 -> 모두 환경/상태이죠.
# 
# 2. 근데 왜 Context가 중요할까요?
# 문제는 이런 상태가 영원히 유지되면 안 된다는 것이기 때문입니다.
# 파일을 열었다면 닫아야 하고, Lock을 얻었다면 풀어야 하고, DB Transaction을 시작했다면 종료해야 하고, Connection을 열었다면 닫아야 합니다.
# 대부분은 다음과 같은 구조를 가집니다. -> 자원/환경 준비 -> Context 진입 -> 작업 수행 -> Context 종료 -> 자원/환경 정리 (이 패턴 중요하니 기억해두시길 바랍니다.)
# 
# 3. Context를 이해할 때 범위(scope)라는 관점도 중요합니다. 다음과 같은 예를 들어보겠습니다.
# Context 진입
print("work 1") # work 1
print("work 2") # work 1
print("work 3") # work 1
# Context 종료
# 여기서 가운데 작업들이 특정 Context 안에서 실행되는 것입니다.
# ┌────────────── Context ──────────────┐
# │                                     │
# │          작업이 실행되는 영역            │
# │                                     │
# └─────────────────────────────────────┘
#
# 4. Context와 Context Manager를 구분하는 것도 중요합니다.
# Context는 환경 또는 상태를 말하고, Context Manager는 그 환경의 시작과 종료를 관리하는 관리자라고 생각하셔야 합니다.
# 
# 5. 그렇다면 Context Manager가 해야 할 일을 알아보겠습니다.
# 들어갈 때: Context 진입(ex. 파일 열기, Lock 획득, DB Transaction 시작)
# 나올 때: Context 종료(ex. 파일 닫기, Lock 해제, Transaction 종료)
# 그래서 Python은 이런 역할을 위한 프로토콜을 제공해줍니다. -> __enter__(), __exit__()

# [ Context Manager는 무엇인가? ]
# Context Manager는 특정 작업 환경(Context)에 들어갈 때 필요한 준비를 하고, 그 환경을 빠져나올 때 필요한 정리 작업을 자동으로 관리하는 객체(관리자)입니다.
# 즉, 작업이 이루어지는 환경의 시작과 종료를 관리하는 객체입니다.
# 
# 1. Context Manager는 왜 필요한가?
# 자원 준비 -> 작업 수행 -> 자원 정리를 하다가 중간에 예외가 발생한다면 어떨 것 같나요? 그럼 최종적으로 Context를 종료하지 못하게 됩니다.
# 그래서 Python에서는 이런 준비 -> 작업 -> 정리 패턴 자체를 객체가 관리하도록 만들 수 있게 해줍니다. 그 객체가 바로 Context Manager입니다.
# 
# 2. 그래서 Python에서는 어떻게 Context Manager를 만드는가?
# Python은 Context Manager를 만들기 위한 프로토콜(protocol)을 정의하고 있습니다. -> __enter__(), __exit__() 메소드들입니다.
# 아래 객체로 Context Manager로 사용할 수 있는 구조를 갖추게 되는 거죠.
class CustomContextManager: # Context Manager Protocol (조건: __enter__(), __exit__() (필수 구현))
    # __enter__(): Context에 진입할 때 수행할 작업을 담당
    def __enter__(self):
        print("자원을 준비합니다.")

    # __exit__(): Context를 빠져나갈 때 수행할 작업을 담당
    # { __exit__(self, exc_type, exc_value, traceback)에 대한 매개변수 해석 }
    # with 블록 안에서 예외가 발생하면 Python이 그 예외에 대한 정보를 __exit__()의 세 매개변수로 전달됩니다.
    # - exc_type: 어떤 종류의 예외인가? (예외 타입)
    # - exc_value: 예외가 가지고 있는 실제 내용은 무엇인가? (예외 객체)
    # - traceback: 예외가 어디에서 발생했는가? (예외 발생 위치/실행 경로 정보)
    def __exit__(self, exc_type, exc_value, traceback):
        # 예외가 발생했을 경우
        if exc_type is not None: # 예외가 없을 때는 exc_type이 None입니다.
            print("예외 발생!") # 예외 발생!
            print("종류: ", exc_type) # <class 'ValueError'>
            print("내용: ", exc_value) # 문제 발생
        
        print("자원을 종료합니다.")

# Context Manager의 중요한 특징 중 하나는 예외가 발생해도 __exit__()가 실행된다는 점입니다.
# 그래서 Context Manager는 자원 정리에 굉장히 유용합니다.
with CustomContextManager():
    print("작업 시작")
    raise ValueError("문제 발생")

# Context Manager는 try-finally문과 연관성이 있습니다.
# resource = acquire()
# try:
#     use(resource) -> 자원을 얻는 과정
# finally:
#     release(resource) -> 자원을 정리하는 과정
# 즉, Context Manager는 이 패턴을 객체의 프로토콜로 추상화한 것이며, 예외가 발생하더라도 종료 작업을 보장하기 위한 객체라고 설명해도 됩니다.

# 설명하기에 아래와 같은 좋은 예시가 있습니다.
with open("../../test/files/hello.txt", "r") as file:
    file.close()
# [open() -> 파일 객체 반환 -> 그 파일 객체가 Context Manager Protocol 지원 -> with가 Context Manager로 사용]흐름으로 동작하기 때문입니다.
# open() 함수 자체가 Context Manager인 게 아니라, open() 함수가 반환하는 파일 객체가 Context Manager로 동작할 수 있는 것입니다. (헷갈리니 중요)

# Context Manager의 진짜 핵심은 '생명주기(Lifecycle) 관리'라고 볼 수 있겠습니다.
# Context Manager = 특정 작업의 생명주기를 관리

# 최종 정리하자면 Python에서 Context Manager Protocol을 구현한 객체를 Context Manager라고 볼 수 있으며, 그에 대한 핵심은 __enter__(), __exit__() 이 매직 메소드들입니다.
