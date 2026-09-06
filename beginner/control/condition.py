# [ 조건문(if, elif, else) ]

# 조건문의 기본 구조
# if 조건:
#    실행할 코드

from typing import Any

user: dict[str, Any] = {
    "name": "Kyungmin Kim",
    "age": 19
}

# [ 기본 if ]
if (age_frist := user["age"]) < 20: # 만약에 age가 20보다 작다면 아래 코드를 실행 (= 만약에 유저의 나이가 성인이 아니라면 아래 코드 실행)
    print(f"{age_frist}세는 미성년자입니다.")

# [ if-else ] (else: 그 조건이 거짓일 때)
if age_frist >= 20:
    print(f"{age_frist}세는 성인입니다.")
else: # 조건이 거짓일 때
    print(f"{user["name"]}는 {age_frist}세이므로 미성년자입니다.")

# [ if-elif-else ] (elif: 여러 개의 조건을 검사)
score = 85

if score >= 90: # score의 점수가 90점 보다 크거나 같을 때
    print("A 학점")
elif score >= 80: # score의 점수가 80점 보다 크거나 같을 때
    print("B 학점")
elif score >= 70: # score의 점수가 70점 보다 크거나 같을 때
    print("C 학점")
else: # 모든 조건에 부합하지 않을 때
    print("F 학점")

# [ 논리 연산자(Logical Operator) 사용 ]
logged_in: bool = False

# not
if not logged_in:
    print("로그인이 필요합니다.")

adult_age = 20
student = False

# and, or
if ((age_second := adult_age) >= 20) and student: # 나이가 20살 이상이며 학생인 사람 판별
    print(f"{age_second}세 학생입니다.")
elif age_second >= 20 and not student: # 나이가 20살 이상이지만 학생이 아닌 사람 판별
    print(f"{age_second}세이지만 학생은 아닙니다.") # 출력
elif age_second < 20 or student: # 나이가 20살 미만인 학생이지만 고등학생/자퇴생 구분 없어도 고등학생이라고 치부함 (or 연산자이기 때문에 하나만 True이면 통과)
    print("고등학생입니다.")

# [ 조건식에서 자료형 활용 ]
username = ""

# Python에서는 0, "", [], {}, None 등이 조건에서 False처럼 취급됩니다. 
if username:
    print("로그인이 되어있습니다.")
else:
    print("로그인이 필요합니다.")

# in 연산자 활용
servers = ["web", "db", "cache"]

if "web" in servers:
    print("웹 서버가 존재합니다.")

# is 연산자 활용
value = None

if value is None:
    print("값이 없습니다.")

# [ 삼항 연산자 ]
age_third = 30

# 형식: (참일 때 값) if (조건) else (거짓일 때 값)
result = "성인" if age_third >= 20 else "미성년자"
print(f"{age_third}세는 {result}입니다.")

# [ match-case문 ] (= Java의 switch문이랑 동일)

# 형식: 
# match 변수:
#   case 패턴1:
#        실행할 코드
#   case 패턴2:
#        실행할 코드
#   case _:
#        실행할 코드

grade = "B"

match grade:
    case "A":
        print("탁월한 성적입니다.")
    case "B":
        print("우수한 성적입니다.") # 출력
    case "C":
        print("보통입니다.")
    case _:
        print("노력이 필요합니다.")

# 동시에 처리하기
match grade:
    case "A" | "B" | "C":
        print("합격입니다.")
    case _:
        print("불합격입니다.")
