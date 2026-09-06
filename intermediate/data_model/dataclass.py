# [ 데이터 클래스(Data Class) ] (= Java의 @DTO 어노테이션과 동일)
# 데이터를 담는 객체를 편하게 만드는 기능입니다.

# { @dataclass가 해주는 일 }
# @dataclass는 단순히 __init__()만 만들어주는 것이 아닙니다.
# Python이 여러 메서드를 자동으로 만들어줍니다. __init__(), __repr__(), __eq__() 등
# @dataclass에서 __init__() -> 개발자가 직접 작성하지 않아도 자동 생성됩니다.

# 일반 클래스(Class)
class UserClass:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# 데이터 클레스(Data Class)
# 데이터 클래스는 '해당 클래스는 주로 데이터를 표현하기 위한 클래스입니다.'라고 Python에게 알려줍니다.
# 그래서 dataclass는 흔히 DTO, 데이터 객체, 설정 객체, API 요청/응답 데이터 등을 표현할 때 사용합니다.
from dataclasses import dataclass, field

# { 주요 사용 설정들 }
# - field(): 해당 필드를 dataclass가 어떻게 다룰지 설정하는 도구
# - default_factory: 객체 생성 시 함수를 호출해서 새로운 값을 만듦 (list, dict, set 같은 mutable 객체의 기본값을 만들 때 사용)
# - frozen=True: 객체를 불변(immutable)처럼 만드는 기능 (한번 만들어진 객체의 상태를 변경하지 않도록 하고 싶을 때 사용)
#   (list에 값을 대입할 경우 -> frozen=True는 필드에 새로운 객체를 대입하는 것을 막는 것이지, list 내부까지 불변으로 만드는 것은 아닙니다.)
# - order=True: 객체 간 순서 비교 (필드 기준)
# - slots=True: Python은 __slots__를 사용하는 형태로 클래스를 생성 (정해진 속성만 관리하도록 제한)
# - __post_init__(): 기본 생성자를 생성하고 추가 작업을 하고 싶을 때 사용 (dataclass는 자동으로 __init__()을 만들어줍니다.)
#   (대표적으로 검증(validation)에 사용할 수 있으며, 값 가공에도 사용 가능합니다.)
# - init=False: 자동 생성되는 __init__()의 매개변수에는 포함하지 않습니다.

# frozen=True는 객체를 생성하고 수정을 불가하게 만드는 설정입니다.
# order=True는 기본적으로 필드 선언 순서대로 비교합니다.
@dataclass(frozen = True, order = True, slots = True)
class UserDataClass:
    name: str = field(compare = False) # compare=False 설정은 객체 비교에 사용되지 않는다는 뜻입니다.
    # 단, 이렇게 Type Hint가 있다고 해서 런타임에 자동으로 타입 검사가 되는 것은 아닙니다.
    # age는 int로 사용하는 것이 의도되어 있음을 알려주는 타입 정보입니다.
    age: int = field(default = 0) # age field의 기본값은 0이라는 뜻입니다.
    active: bool = field(init = False) # 기본 생성자 초기화에 들어가지 않는 필드
    tags: list[str] = field(default_factory = list) # User 객체가 만들어질 때마다 list()를 호출해서 새로운 리스트를 만든다는 뜻입니다. (default_factory는 값이 아니라 호출할 함수를 전달합니다.)

    def __post_init__(self):
        print("UserDataClass 생성 완료")

user = UserDataClass("Kim", 20) # 객체 생성
# getter 가능
print(user.name) # Kim
print(user.age) # 20

# setter 가능
# user.name = "Kyungmin" # frozen = True를 설정해줬기 때문에 변경이 불가합니다.
print(user.name) # Kyungmin

user1 = UserDataClass("Kim", 20)
user2 = UserDataClass("Lee", 30)

print(user1 < user2) # True
print(user1 > user2) # False
