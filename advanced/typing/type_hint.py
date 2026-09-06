# [ 타입 힌트(Type Hint) ]
# Type Hint = 변수, 함수의 매개변수, 반환값 등에 어떤 타입을 기대하는지 표시하는 문법입니다.

# '이 변수에는 이런 타입의 값이 들어올 것으로 예상한다.'라는 의미로 표현하는 것입니다.
name1: str = "Kim" # str type
age1: int = 20 # int type
height: float = 175.5 # float type

# 여기서 중요한 점이 있습니다.
# Python은 Type Hint가 있어도 동적 타입 언어입니다. 동적 타임 언어이기 때문에 아래와 같이 코드를 작성해도 실핼할 때는 에러를 주지 않습니다.
age2: int = 20
# age2 = "hello" # 본 필자 IDE에서 에러(밑줄)가 나기 때문에 잠시 주석으로 처리하겠습니다.
print(age2) # hello (Python은 기본적으로 실행할 때 Type Hint를 강제하지 않습니다.)
# 즉, 강제 규칙이 아니라 타입 정보/힌트로 표현하는 것입니다.

# { Type Hint는 왜 사용하는가? }
def add(a: int, b: int) -> int:
    return a + b
# a: int를 기대, b: int를 기대, return: int를 반환할 것으로 기대
# 즉, 정보를 코드에 표현한 것에 가깝습니다.

# { ->은 뭘까요? }
# ->은 반환 타입(Return Type)입니다.
def subtract(a: int, b: int) -> int: # 'int type으로 반환할 예정이다.'라는 것을 명시해줍니다.
    return a - b

# 반환값이 없다면 None을 사용할 수 있습니다.
def print_name(name: str) -> None:
    print(name)

# { |(Optional)를 이용한 여러 타입 }
value1: int | str # value는 int 또는 str
# 둘 다 타입 힌트상 허용됩니다.
value2: int | str = 10
value3: int | str = "hello"

# { Optional과 None }
name2: str | None # str 또는 None이라는 의미입니다.
# 사용자를 찾으면 str을 반환하고, 없으면 None을 반환할 수 있습니다.
def find_user(user_id: int) -> str | None:
    pass

# [ 최종 정리 ]
# Type Hint는 Python 코드에서 변수, 매개변수, 반환값 등의 예상 타입을 표현하여 코드의 의도를 명확하게 하고, IDE와 Type Checker가 정적 분석을 할 수 있도록 하는 타입 정보입니다.
# 중요한 포인트는 Type Hint가 있다고 해서 Python이 자동으로 타입을 강제하는 것은 아니라는 것을 꼭 기억하시길 바랍니다.
