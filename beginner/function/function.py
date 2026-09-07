# [ 함수(Function) ]
# 
# { 형식 }
# def function_name(parameter) -> type hint:
#     code to run
# type hint는 반환 값을 미리 정의해주는 것이며, 생략 가능합니다.
#
# 본 필자는 Java/Kotlin을 먼저 공부했기 때문에 반환할 값을 미리 정의해두는 게 좋아서 type hint를 사용할 예정입니다.
# (언어 차원에서 타입 추론을 해주기 때문에 굳이 안 써도 됩니다.)
# 
# { 들어가기 전 }
# 매개변수(parameter)와 인수(arguments)는 혼용해서 사용하는 용어이므로 잘 기억해두면 좋을 것 같습니다.
#
# 매개변수(parameter): 함수에 입력으로 전달된 값을 받는 변수
# 인수(arguments): 함수를 호출할 때 전달하는 입력값

# { 매개변수 없는 간단한 기본적인 함수 }
def hello_frist() -> None:
    print("Hello, Python!") # (terminal print: Hello, Python!)

# 함수 호출하여 동작 실행
hello_frist()

# 문제) 구구단 함수
def times_tables(num: int) -> None: # 반환 값이 없는 함수는 type hint가 없어도 됩니다.
    for j in range(1, 10):
        # 여기서 사용하는 num은 매개변수(parameter)입니다.
        print(f"{num} x {j} = {num * j}") # (terminal print: 2단 출력)

# 구구단 함수 호출
times_tables(2) # 여기서는 인수(arguments)라고 불립니다.

# { 반환(return) }
def f1(x) -> int: # 매개변수를 넣으면 내부에서 계산하여 값을 반환해주는 함수
    a, b = 5, 3 # 변수 선언
    result = a * x + b # 최종 계산

    return result # 반환

# 함수를 호출하고 반환 값을 result_first에 대입해 줍니다.
result_first = f1(x = 10) # 필수는 아니지만 명시적으로 매개변수를 지정하여 호출하는 방법도 있습니다.
print(result_first) # (terminal print: 53)

# { print(result)랑 return result의 차이점 }
# 1. print(result)
def f2(x) -> None:
    a, b = 6, 2 # 변수 선언
    result = a * x + b # 최종 계산

    print(result) # 98

# 함수 호출함과 동시에 함 수 내부 print() 실행
result_second = f2(16)
print(result_second) # (terminal print: None) 출력만 하고 반환 값이 없으니 None으로 출력됩니다.

# 2. return result
def f3(x) -> int:
    a, b = 6, 2 # 변수 선언
    result = a * x + b # 최종 계산

    return result

result_third = f3(16) # 함수를 호출하고 반환 값을 result_third에 대입해 줍니다.
print(result_third) # (terminal print: 98)

# { 참(True)과 거짓(False) }
# 12를 입력하면 True, 그 외 숫자를 입력하면 False를 반환합니다.
def quiz() -> bool:
    q = input("2 x 6 = ") # 사용자의 입력을 받는 input() 함수를 사용하여 문제를 풀도록 합니다.
    return 2 * 6 == int(q) # 사용자가 입력한 문자를 int() 함수를 사용하여 int type으로 만들고 실제 연산과 비교하여 값을 반환합니다.

result_fourth = quiz() # 함수 호출과 동시에 사용자의 입력을 받음
print(result_fourth) # (terminal print: True) 12: True, 그 외: False
