# [ 논리 연산자(Logical Operator) ]
# not 연산자: not 연산자는 True를 False로, False를 True로 바꿉니다.
# or 연산자: or 연산자는 두 개의 피연산자 중 하나라도 True이면 True를 반환합니다.
# and 연산자: and 연산자는 두 개의 피연산자가 모두 True이면 True를 반환합니다. 하나라도 False이면 False를 반환합니다.

is_active_first: bool = True
is_active_second: bool = False

print(f"and 연산: {is_active_first and is_active_second}") # False
print(f"or 연산: {is_active_first or is_active_second}") # True
print(f"not 연산: {not is_active_first}") # False

# [ 산술 연산자(Arithmetic Operator) ]
# Python의 산술 연산자는 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/(실수형 몫), //(정수형 몫), %(나머지)), 거듭제곱(**) 연산자가 있습니다.

a: int = 10
b: int = 5

print(f"(덧셈) a + b = {a + b}") # 15
print(f"(뺄셈) a - b = {a - b}") # 5
print(f"(곱셈) a x b = {a * b}") # 50
print(f"(나눗셈) a ÷ b = {a / b} (몫(실수))") # 2.0 (Python의 /는 항상 나눗셈 결과를 실수(float)로 반환합니다.)
print(f"(나눗셈) a ÷ b = {a // b} (몫(정수))") # 2 (/ 했을 때 실수(float)로 반환되는 것을 방지하기 위해 //를 사용하면 몫(정수)로 반환됩니다.)
print(f"(나눗셈) a ÷ b = {a % b} (나머지)") # 0
print(f"(거듭제곱) a ** b = {a ** b}") # 100000 (= 10의 5승)

# [ 비교 연산자(Comparison Operator) ]
# Python의 비교 연산자는 같음(==), 다름(!=), 크거나 같음(>=), 작거나 같음(<=), 작음(<), 큼(>) 연산자가 있습니다. (Java와 동일)

c: int = 20

print(f"(같음) c = 20: {c == 20}") # True
print(f"(다름) c != 21: {c != 20}") # False
print(f"(크거나 같음) c >= 20: {c >= 20}") # True
print(f"(작거나 같음) c <= 20: {c <= 20}") # True
print(f"(작음) c < 21: {c < 21}") # True
print(f"(큼) c > 19: {c > 19}") # True

# [ 대임 연산자(Assignment Operator) ]

# 계산을 위한 초기 변수
d = 32 # 나중에 나눗셈(/=) 연산을 하면 float type이 나오기 때문에 타입 유추로 선언해 주겠습니다.

# d = 기존 값 + 2
d += 2
print(f"32 + 2 = {d}") # 34

# d = 기존 값 - 2
d -= 2
print(f"34 - 2 = {d}") # 32

# d = 기존 값 x 4
d *= 4
print(f"32 x 4 = {d}") # 128

# d = 기존 값 ÷ 2
d //= 2
print(f"(몫(정수)) 128 ÷ 2 = {d}") # 64

# d = 기존 값 ÷ 2
d /= 2 # (/= 연산이기 때문에 float type이 나와 실수로 표시됩니다.)
print(f"(몫(실수)) 64 ÷ 2 = {d}") # 32.0

# d = 기존 값 ÷ 3 (나머지)
d %= 3
print(f"(나머지) 32.0 ÷ 3 = {d}") # 2.0

# d = 기존 값의 2승
d **= 2
print(f"2.0의 3승: {d}") # 4.0

# 바다코끼리 연산자(Walrus Operator)라고 불리는 대입 연산자가 있습니다. (:= 키워드 사용)
# 초반에는 굳이 사용할 필요 없지만 알아두면 좋을 것 같아 작성합니다.
message: str = "Hello, Python!" # total 14 words

# message 변수의 문자열 길이를 length에 대입하고 length가 12보다 클 때 print를 출력하게 작성하였습니다.
if (length := len(message)) > 12:
    print(f"total words: {length} words") # 14

# [ 멤버십 연산자(Membership Operator) ]
# 특정 값이나 요소가 list, tuple, str, dict 같은 자료형에 포함되어 있는지 확인하는 연산자입니다. (in 키워드 사용)
names: list[str] = ["Kim", "Lee", "Park"]

print("Kim" in names) # True ("Kim"이 names 안에 있는가?를 질의하는 코드입니다.)
print("Choi" not in names) # True ("Choi"가 names 안에 없는가?를 질의하는 코드입니다.)

from typing import Any

users: dict[str, Any] = {
    "name": "Kyungmin",
    "age": 20
}

print("name" in users) # True (dict에서는 기본적으로 key로 검색을 합니다.)

# [ 식별 연산자(Identity Operator) ]
x = None # (None은 null과 동일)

if x is None:
    print("값이 없습니다!")
elif x is not None: # 변수 x가 None이 아니면 실행됩니다.
    print("값이 있습니다!") # 출력 안 됨

# 중요!! == 연산자와 is 연산자는 동일한가? -> X
# == 연산자는 값이 같은지를 판별합니다. (일반적으로 값 비교에서 사용합니다.)
y = [1, 2, 3]
z = [1, 2, 3]

print(y == z) # True

# is 연산자는 같은 객체인지 판별합니다. (객체의 동일성에 사용됩니다.)
print(y is z) # False

# [ 비트 연산자(Bitwise Operator) ]
# 컴퓨터는 숫자를 내부적으로 2진수(Binary)로 표현하기 때문에 비트 연산자는 주어진 값을 각각 0, 1을 대상으로 연산합니다.
num_frist: int = 7 # (= 0000 0111)
num_second: int = 5 # (= 0000 0101)

# AND(&) 연산 설명
#   7 = 0111
# & 5 = 0101
# ----------
#       0101(= 5)
# 둘 다 1인 상태여야 함으로 1 0은 0으로 연산됩니다. (1 0: X, 1 1: O)
print(num_frist & num_second) # 5

# OR(|) 연산 설명
#   7 = 0111
# | 5 = 0101
# ----------
#       0111(= 7)
# 둘 중 하나만 1인 상태여도 되므로 1 0도 1로 연산됩니다. (1 0: O, 1 1: O)
print(num_frist | num_second) # 7

# XOR(^) 연산 설명
#   7 = 0111
# ^ 5 = 0101
# ----------
#       0010(= 2)
# 서로 다르면 1로 연산합니다. (1 1: X, 0 0: X, 1 0: O) 즉, 같다면 0, 다르면 1로 연산합니다.
print(num_frist ^ num_second) # 2

# NOT(~) 연산 설명
# 참고! Python의 int는 고정된 8bit / 32bit 정수가 아닙니다. 즉, 메모리가 허용하는 한 숫자의 크기에 제한 없이 무한히 큰 정수를 표현할 수 있습니다.
# (단, 본 설명에서는 8bit로 표현하겠습니다.)
#
# { 용어 정리 }
# unsigned: 음수를 허용하지 않으며, 양수만 사용 가능합니다. 음수를 쓰지 않는 대신, 표현할 수 있는 양수의 최대 범위를 두 배로 늘립니다.
# signed: 양수, 음수, 0을 모두 표현할 수 있습니다. 가장 왼쪽 비트를 부호 비트로 사용합니다. (0이면 양수, 1이면 음수) !!
#
# { 내부 동작 원리 }
# 1) 7 = 0000 0111, 비트를 모두 반전하면 ~7 = 1111 1000
#   이 비트 패턴을 unsigned로 해석하면 248이지만, signed 2의 보수 방식으로 해석하면 -8입니다. 
#   (프로그래밍 언어에서 signed 2의 보수 방식으로 해석할 때는 맨 앞 비트가 1이면 음수 영역이라고 약속하였습니다.)
# 
# 2) 2의 보수에서 음수의 절댓값(크기)을 구하는 방법은 다음과 같습니다.
#   1. 비트를 모두 뒤집는다.
#   2. 1을 더한다.
#
#   1111 1000
#   ↓ 비트 반전
#   0000 0111
#   ↓ +1 -> 0111(= 7) + 0001(= 1) = 1000(= 8) -> AND 연산이라고 생각하면 안 되며, 산술 연산의 더하기(+)를 생각하셔야 합니다.
#   0000 1000
#   = 8
#
#   따라서 1111 1000 = -8
#   결과적으로 ~x = -(x + 1) 관계식을 기억하면 됩니다. (쉬움)
print(~num_frist) # -8

# << 연산자는 왼쪽으로 비트를 이동시킵니다.
# 7 = 0000 0111
# 5 = 0000 0101
# 여기서 num_second만큼 켜진 비트를 왼쪽으로 밀어줍니다. 즉, 1110 0000
# 켜진 비트만 더해 보자면 128 + 64 = 192 + 32 = 224가 나오는 것을 볼 수 있습니다.
print(num_frist << num_second) # 224

# >> 연산자는 오른쪽으로 비트를 이동시킵니다.
# 7 = 0000 0111
# 5 = 0000 0101
# 여기서 num_second만큼 켜진 비트를 오른쪽으로 밀어줍니다. 즉, 0000 0000
# 켜진 비트가 없기 때문에 0이 됩니다.
print(num_frist >> num_second) # 0

# [ 비트 연산자(Bitwise Operator) - 비트 마스킹(Bit Masking) ]
# 어떤 숫자의 특정 비트가 켜져 있는지 확인할 수 있으며, 이를 비트 마스킹(Bit Masking)이라고 합니다.
value = 6
mask = 2

# value = 0110(= 6)
# mask = 0010(= 2)
# 
#    0110
# &  0010
# --------
#    0010(= 2) -> 두 번째 비트가 켜져 있음을 알 수 있습니다.
if value & mask:
    print(f"두 번째 비트가 켜져 있습니다.") # 두 번째 비트가 켜져 있습니다.

# [ 비트 연산자(Bitwise Operator) - 응용 ]
# 문제. IP 주소 192.168.10.8의 네트워크 주소를 구하시오. (Subnet Mask = 255.255.255.240(= CIDR /28))

ip: list[int] = [192, 168, 10, 8]
subnet_mask: list[int] = [255, 255, 255, 240]

net_value = ip[3]
net_mask = subnet_mask[3]

# AND(&) 연산 내부 동작
# 
# ip[3] = 8(= 1000)
# subnet_mask[3] = 240(= 1111 0000)
# 
#    0000 1000
# &  1111 0000
# -------------
#    0000 0000(= 0)
# 
# 따라서 192.168.10.8의 네트워크 주소는 192.168.10.0이 됩니다.
print(f"Network Address: {ip[0]}.{ip[1]}.{ip[2]}.{net_value & net_mask}") # 192.168.10.0
