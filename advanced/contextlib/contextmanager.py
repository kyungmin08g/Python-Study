# [ @contextmanager ]
# = Context Manager를 클래스를 만들지 않고 함수 하나로 구현하게 해주는 도구입니다.
# @contextmanager를 사용하면 __enter__()와 __exit__()를 직접 구현하지 않고도 Context Manager를 만들 수 있습니다.

# { 기존 Context Manager 사용 }
# 그런데 단순한 Context Manager 하나 만들려고 매번 클래스를 작성하는 건 번거롭습니다. 
# 이를 해결하기 위해서 @contextmanager가 등장한 것입니다.
class Database:
    def __enter__(self):
        print("(base) DB 연결")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("(base) DB 연결 종료")

with Database() as db:
    print("(base) DB 작업")

# { @contextmanager 사용 }
# 클래스도 없고 __enter__(), __exit__()도 직접 작성하지 않았지만 기존 Context Manager랑 동일하게 동작합니다.
from contextlib import contextmanager

@contextmanager
def database():
    # 진입
    print("(contextmanager) DB 연결")

    # 실제 잡업
    yield db # yield는 with 블록의 앞뒤를 나누는 경계라고 생각하면 이해하기 쉽습니다.
    # yield는 값을 전달할 수도 있습니다. 위 코드에서는 yield db가 as db로 전달되는 것입니다.

    # 종료
    print("(contextmanager) DB 연결 종료")

with database():
    print(f"(contextmanager) DB 작업: {db}") # <__main__.Database object at 0x102e29fd0>

# @contextmanager는 무엇을 할까요?
# contextlib.contextmanager가 이 generator 함수를 Context Manager 객체로 변환해줍니다. (* generator를 꼭 공부하셔야 이번 챕처가 이해됩니다.)
# @contextmanager는 Context Manager Protocol을 없애는 게 아니라, 그 구현을 대신 작성해주는 편의 기능입니다.
# 자세한 사항은 Context Manager 패키지에서 공부했으므로 넘어가겠습니다.
