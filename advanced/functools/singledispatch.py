# [ singledispatch ]
# singledispatch는 첫 번째 인자의 타입에 따라 실행할 함수 구현을 선택하는 기능입니다.

# { 예제 }
from functools import singledispatch, singledispatchmethod

# { singledispatch }
@singledispatch
def process(value):
    print("기본 처리")

# 여러 타입을 한 구현에 등록할 수도 있습니다.
@process.register(int)
@process.register(float)
def _(value: int):
    print("숫자 처리")

@process.register
def _(value: str):
    print("문자열 처리")

process(10)
process("hello")
process(3.14)

# { singledispatchmethod }
# singledispatchmethod는 클래스 메소드 위치에 선언하는 겁니다.
class Processor:

    @singledispatchmethod
    def process(self, value):
        print("기본 처리")

    @process.register
    def _(self, value: int):
        print("정수 처리")

    @process.register
    def _(self, value: str):
        print("문자열 처리")

# { 왜 이런 기능이 필요할까요? } - 메서드 오버로딩(Method Overloading)
# Java에서는 같은 이름의 메서드를 매개변수 타입에 따라 여러 개 정의할 수 있었습니다.
# void process(int value) {
#     ...
# }

# void process(String value) {
#     ...
# }
# 이것을 메서드 오버로딩(Method Overloading)이라고 합니다.
# 컴파일러가 인자의 타입을 보고 어떤 메서드를 사용할지 결정하는 역할을 합니다. 하지만 Python은 기본적으로 이런 식의 정적 함수 오버로딩을 제공하지 않습니다.
# 만약 아래와 같은 코드가 있다고 해보겠습니다.
# def process(value: int):
#     print("int")
# 
# def process(value: str):
#     print("str")
# 위 두 함수가 동시에 존재하는 게 아니고 두 번째 process()가 첫 번째 process()를 덮어씁니다.
# 이를 singledispatch가 해결하는 겁니다.
# @singledispatch를 선언하면 일반 함수이면서 타입별 구현을 등록할 수 있는 dispatch 함수로 변환됩니다.
# 
# 중요한 것은 타입 힌트입니다. 강제하는 것이 아니라 int 타입이 들어오면 -> 이 구현을 사용하겠다는 의미로 사용됩니다.
# 
# { 실제 dispatch 과정 }
# [ process(10) -> 첫 번째 인자의 타입 확인 -> type(10) -> int -> int용 구현이 등록되어 있는가? -> YES -> int 구현 실행 ] 흐름으로 동작합니다.
# 그래서 이름은 single-dispatch입니다. 첫 번째 인자 하나를 기준으로 dispatch한다는 의미죠.

# Python의 오버로딩과는 조금 다릅니다.
# Java처럼 함수의 시그니처 자체가 여러 개 존재하는 것이 아닙니다.
# 즉, Java/C++의 전통적인 오버로딩과 완전히 동일한 것은 아니며, 런타임에 첫 번째 인자의 타입을 기준으로 구현을 선택하는 것입니다.
# - Java Overloading: 컴파일 시점의 정적 선택
# - singledispatch: 런타임의 동적 dispatch
