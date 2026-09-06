# [ partial ]
# 함수의 일부 인자를 미리 고정해서 새로운 함수를 만드는 것입니다.

# { 일반 함수 사용 }
def add(a, b):
    return a + b

# 아래와 같이 계속 a에 10을 넣는다면 귀찮아지지 않을까요? 이 문제를 해결하기 위해 partial이 나왔습니다.
add(10, 20)
add(10, 30)
add(10, 40)

# { partial 사용 }
from functools import partial

# 형식: partial(함수, 미리 넣을 인자)
add_10 = partial(add, 10)
# 위 코드는 아래 주석된 코드와 같은 기능을 합니다.
# def add_10(b):
#     return add(10, b)

print(add_10(10)) # 20
print(add_10(20)) # 30
print(add_10(30)) # 40

# 여러 개의 인자를 고정할 수도 있습니다. (위치 기반)
def multiply(a, b, c):
    return a * b * c

multiply_2_3 = partial(multiply, 2, 3) # (= multiply(2, 3, 4))

print(multiply_2_3(4)) # 24

# 키워드 인자도 고정할 수 있습니다. (키워드 기반)
def greet(name, message):
    return f"{message}, {name}!"

hello = partial(greet, message="Hello") # message로 지정해서 값을 넣을 수 있습니다.

print(hello("철수")) # Hello, 철수!
print(hello("영희")) # Hello, 영희!
# partial을 사용하면 반복되는 인자를 미리 고정할 수 있습니다.

# [ 중요한 점 ]
# partial은 새로운 함수를 만듭니다.
# add_10은 그냥 10이라는 값이 아닙니다. 호출할 수 있는 새로운 객체(callable)입니다.
# 즉, add -> partial -> 새로운 callable -> add_10 순으로 동작합니다.
print(add_10(5)) # 15
print(callable(add_10)) # True

# [ 클로저와 partial의 차이 ]
# 클로저 - 새로운 함수의 동작 자체를 정의 ("이 함수는 이렇게 동작해야 해") -> 새로운 함수의 로직을 직접 구성
def make_adder(x):
    def add_x(y):
        return x + y
    return add_x

# partial - 기존 함수를 그대로 활용하면서 ("이 함수의 인자 중 일부만 미리 고정할게") -> 기존 함수 + 일부 고정된 인자
add_10 = partial(add, 10)

# partial을 사용하면 코드가 깔끔해지는 경우가 있습니다.
def log(level, message):
    print(f"[{level}] {message}")

# 일반적인 방식
log("ERROR", "파일을 찾을 수 없습니다.") # [ERROR] 파일을 찾을 수 없습니다.
log("ERROR", "권한이 없습니다.") # [ERROR] 권한이 없습니다.
log("ERROR", "연결이 실패했습니다.") # [ERROR] 연결이 실패했습니다.

# partial 방식
error_log = partial(log, "ERROR")
error_log("파일을 찾을 수 없습니다.") # [ERROR] 파일을 찾을 수 없습니다.
error_log("권한이 없습니다.") # [ERROR] 권한이 없습니다.
error_log("연결이 실패했습니다.") # [ERROR] 연결이 실패했습니다.
# 이런 식으로 특정 설정을 미리 고정한 함수를 만들 때 유용합니다.

# [ partial 객체 내부 ]
# partial 객체에는 미리 고정한 정보가 들어 있습니다.
# - func: 원본 함수 add
# - args: 미리 고정한 위치 인자 (10,)
# - keywords: 미리 고정한 키워드 인자
print(add_10.func) # <function add at 0x109921dd0>
print(add_10.args) # (10,)
print(add_10.keywords) # {}

# [ 최종 정리 ]
# functools.partial은 기존 함수의 일부 인자를 미리 고정하여, 나머지 인자만 받아 호출할 수 있는 새로운 callable을 생성하는 도구입니다.
# (고차 함수 -> 함수를 객체처럼 전달 -> partial -> 기존 함수에 인자를 미리 바인딩 -> 새로운 callable 생성)
