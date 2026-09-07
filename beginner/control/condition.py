# [ 조건문(if, elif, else) ]
# 조건문은 조건이 있을 경우 그에 대한 코드를 동작하도록 하는 문법이며, 기본 형식는 다음과 같습니다.
# 
# { 형식 }
# if 조건:
#    실행할 코드

# 조건문 예제를 위한 변수 등록 (예제 준비)
from typing import Any

user: dict[str, Any] = { "name": "Kyungmin", "age": 19 }

# { 기본 if } - if: 조건이 있을 경우
if (age_frist := user["age"]) < 20: # 만약에 age가 20보다 작을 경우 (= 만약에 유저의 나이가 성인이 아닐 경우)
    print(f"{age_frist}세는 미성년자입니다.") # (terminal print: 19세는 미성년자입니다.)

# { if-else } - else: 모든 조건이 거짓일 경우
if age_frist >= 20:
    print(f"{age_frist}세는 성인입니다.")
else: # 조건이 거짓일 때
    print(f"{user["name"]}은 {age_frist}세이므로 미성년자입니다.") # (terminal print: Kyungmin은 19세이므로 미성년자입니다.)

# { if-elif-else } - elif: 여러 개의 조건을 검사
score = 85

if score >= 90: # score의 점수가 90점 보다 크거나 같을 경우
    print("A 학점")
elif score >= 80: # score의 점수가 80점 보다 크거나 같을 경우
    print("B 학점") # (terminal print: B 학점)
elif score >= 70: # score의 점수가 70점 보다 크거나 같을 경우
    print("C 학점")
else: # 모든 조건에 부합하지 않을 경우
    print("F 학점")

# { 논리 연산자(Logical Operator) 사용 }
logged_in: bool = False
adult_age = 20
student = False

# not
if not logged_in: # True가 아닐 경우 (= False을 경우)
    print("로그인이 필요합니다.") # (terminal print: 로그인이 필요합니다.)

# and, or
if ((age_second := adult_age) >= 20) and student: # 나이가 20살 이상이며 학생인 사람일 경우
    print(f"{age_second}세 학생입니다.")
elif age_second >= 20 and not student: # 나이가 20살 이상이지만 학생이 아닌 사람일 경우
    print(f"{age_second}세이지만 학생은 아닙니다.") # (terminal print: 20세이지만 학생은 아닙니다.)
elif age_second < 20 or student: # 나이가 20살 미만인 학생이지만 고등학생/자퇴생 구분 없어도 고등학생이라고 치부합니다. (or 연산자이기 때문에 하나만 True이면 통과됩니다.)
    print("고등학생입니다.")

# { 조건식에서 자료형 활용 }
username = ""
servers = ["web", "db", "cache"]
value = None

# Python에서는 0, "", [], {}, None 등이 조건에서 False처럼 취급합니다.
# 현재 username이 ""이기 때문에 False로 판단이 되어 else문으로 넘어갑니다.
if username: # username이 ""가 아닐 경우 (= 뭐라도 써져 있을 경우)
    print("로그인이 되어있습니다.")
else:
    print("로그인이 필요합니다.") # (termainal print: 로그인이 필요합니다.)

# in 연산자 활용
if "web" in servers: # servers list에 "web"이라는 문자열이 있을 경우
    print("웹 서버가 존재합니다.") # (terminal print: 웹 서버가 존재합니다.)

# is 연산자 활용
if value is None: # value가 None일 경우
    print("값이 없습니다.") # (terminal print: 값이 없습니다.)

# [ 삼항 연산자 ]
# 
# { 형식 }
# (참일 때 값) if (조건) else (거짓일 때 값)

age_third = 30

result = "성인" if age_third >= 20 else "미성년자" # age_third가 20보다 크거나 같을 경우 성인을 출력하고 아닐 경우 미성년자를 출력하겠다는 의미입니다.
print(f"{age_third}세는 {result}입니다.") # (terminal print: 30세는 성인입니다.)

# -----------------------------------------------------------------------------------------------
# [ match-case문 ] (= Java의 switch문이랑 동일)
# 
# { 형식 }
# match 변수:
#   case 패턴_1:
#        실행할 코드_1
#   case 패턴_2:
#        실행할 코드_2
#   case _:
#        실행할 코드_3

# 등급 변수
grade = "B"

# 해당 변수에 대한 값에 부합하는 case를 찾고, 그에 맞는 print()문을 실행하는 코드입니다.
match grade:
    case "A":
        print("탁월한 성적입니다.")
    case "B": # grade 변수가 B인 상태이기 때문에 case B로 들어오게 됩니다.
        print("우수한 성적입니다.") # (terminal print: 우수한 성적입니다.)
    case "C":
        print("보통입니다.")
    case _: # _는 기타(etc)를 의미합니다.
        print("노력이 필요합니다.")

# 하나의 case에 여러 조건을 사용할 수 있습니다. (동시에 처리)
match grade:
    case "A" | "B" | "C": # grade가 A, B, C 셋 중 하나만 포함된다면 아래 코드를 실행한다는 의미입니다.
        print("합격입니다.") # (terminal print: 합격입니다.)
    case _: # A, B, C가 아닐 때 해당 case로 들어오게 됩니다.
        print("불합격입니다.")
