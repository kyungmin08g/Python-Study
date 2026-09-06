# [ 제네릭(Generic) ] (= Java의 Generic이랑 동일)
# 제네릭(Generic)은 간단하게 타입을 미리 하나로 고정하지 않고, 사용할 때 타입을 결정할 수 있도록 만드는 것입니다. 또는 타입 자체를 매개변수처럼 다루는 것을 의미합니다.
# list[int], dict[str, int]도 Generic한 타입 표현의 대표적인 예입니다.

# { 예제 }
def identity_first(value):
    return value

# 인수가 Type에 상관없이 아무 Type이나 담길 수 있습니다.
identity_first(10)
identity_first("hello")
identity_first(3.14)

# 하지만 Type Hint를 적용할려고 하면 문제가 생깁니다.
# def identity(value: ???) -> ???:
#     return value
# 만약 value가 int type이나 str type이면 아래와 같이 작성할 수 있죠.
# 
# int type
def identity_second(value: int) -> int:
    return value
identity_second(10)

# str type
def identity_third(value: str) -> str:
    return value
identity_third("Hello")

# 하지만 우리가 원하는 것은 입력으로 들어온 타입을 그대로 반환하는 함수입니다.
# 그것을 위해 제네릭(Generic)이 등장합니다면 제네릭(Generic)을 이해하려면 TypeVar 개념을 필수로 알아야 합니다.
# 
# [ TypeVar ]
from typing import TypeVar

# TypeVar는 Type Variable, 즉 타입 변수입니다. (= 나중에 어떤 타입이 들어올지 정해지지 않은 타입을 가리키는 변수)
# 여기서 T는 특정 타입 하나를 의미하는 타입 변수(Type Variable)입니다.
T = TypeVar("T")

# 해당 함수를 해석하면 'value의 타입을 T라고 하고, 반환값도 같은 T 타입으로 한다.'라는 의미를 지닙니다.
def identity_t(value: T) -> T:
    return value

# T = int
# identity(int) -> int
print(identity_t(10)) # 10

# [ Any와 Generic의 차이 ]
# 절대 헷갈리면 안 됩니다 !!
from typing import Any

# Any는 '이 값은 어떤 타입이든 상관없다.'라는 의미를 지닙니다.
# T는 '어떤 타입인지는 상관없지만, 입력과 출력의 타입 관계는 유지한다.'라는 의미를 지닙니다.
def identity_a(value: Any) -> Any:
    return value
# 즉, Any -> 입력: 뭐든, 출력: 뭐든, 관계: 모름 | T -> 입력: T, 출력: T, 관계: 동일한 타입

# [ 사용자 정의 Generic ]
from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]): # Box라는 클래스는 T라는 타입을 사용하는 Generic 클래스입니다.
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

int_box = Box[int](10) # T = int
int_box.get() # type = int

str_box = Box[str]("hello") # T = str
str_box.get() # type = str

# Python은 Java처럼 정적 타입 언어가 아니기 때문에 Generic은 주로 정적 타입 검사와 IDE의 타입 추론을 위한 정보로 사용됩니다.
# Generic은 기본적으로 Type Hint 시스템의 일부입니다. 즉, 해당 타입을 기대한다는 거죠.
