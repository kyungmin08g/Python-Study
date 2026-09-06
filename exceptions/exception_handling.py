# [ 예외 처리(Exception Handling) ]
# 예외 처리란 프로그램 실행 중 문제가 발생했을 때 프로그램이 어떻게 대응할지를 제어하는 방법을 말합니다.

print("첫 번째 출력")
# 먼저 오류(Error)와 예외(Exception)를 구분해보겟습니다.
# result = 10 / 0 # 이 때 ZeroDivisionError: division by zero라는 예외가 나타납니다.
# 예외는 프로그램이 실행되는 도중에 정상적인 흐름을 더 이상 진행할 수 없는 상황이 발생한 것을 말합니다.
print("두 번째 출력")
# { 출력 결과 }
# 첫 번째 출력
# ZeroDivisionError: division by zero
# 
# 예외가 발생하면서 실행 흐름이 중단되기 때문에 다음 코드는 실행되지 않습니다.
# 즉, print문 출력 -> 10 / 0 실행 -> 예외 발생 -> 현재 함수의 실행 중단 -> 예외를 처리할 곳을 찾음 순으로 진행됩니다.

# { 예외 처리를 사용하는 이유 }
# 예외가 발생했을 떄 프로그램이 중단되거나 종료되는데 그대로 놔두면 될까요?
# 간단한 프로그램이라면 그럴 수도 있지만, 실제 프로그램에서는 문제가 됩니다. 그렇기 때문에 어떻게든 처리해서 다음 코드가 실행되도록 해야합니다.

# [ try-except ]
# 제일 기본적이고 기초적인 문법입니다. (Python의 가장 기본적인 예외 처리 문법이죠.) 형식은 다음과 같습니다.
# try:
#     예외가 발생할 수 있는 코드
# except:
#     예외가 발생했을 때 실행할 코드
try:
    result = 10 / 0 # 예외 발생
    print("계산 완료")
except:
    print("계산 중 오류 발생") # 계산 중 오류 발생
# 위와 같이 try-except 문법은 try 진입 -> 10 / 0 실행 -> 예외 발생 -> try 블록 즉시 중단 -> except 실행 -> "계산 중 오류 발생" 출력 순으로 흘러갑니다.

# [ 특정 예외만 잡고 싶다면? ]
# except를 그냥 사용하면 모든 예외를 잡아버리기 때문에 except 옆에 어떤 예외를 처리할 것인지 명시하는 것이 좋습니다.
try:
    result = 10 / 0
except ZeroDivisionError: # ZeroDivisionError는 Python이 제공하는 예외 클래스입니다.
    print("0으로 나눌 수 없습니다.") # 0으로 나눌 수 없습니다.

# Python에는 굉장히 많은 내장 예외가 있지만 공부할 때는 대표적인 것들만 배우도록 하겠습니다.
# ZeroDivisionError: 0으로 나웠을 떄 발생
# ValueError: 값 형식이 잘못되었을 때
# TypeError: 자료형이 맞지 않을 때
# IndexError: 존재하지 않는 인덱스에 접근했을 때
# KeyError: 딕셔너리에 존재하지 않는 키를 사용했을 때
# AttributeError: 존재하지 않는 속성이나 메서드에 접근했을 때
# FileNotFoundError: 존재하지 않는 파일을 열려고 할 때

# [ 여러 예외 처리하기 ]
try:
    # 숫자를 입력 받고 나눌 수 없는 숫자를 만났을 때는 try문을 닫고 except ZeroDivisionError로 향하여 예외를 발생시킵니다.
    number = int(input("숫자: "))
    result = 10 / number # 0으로 나눌 수 없고, 문자를 받을 수 없습니다.
except ValueError:
    print("숫자를 입력해야 합니다.")
except ZeroDivisionError:
    print("0은 입력할 수 없습니다.")

try:
    result = 10 / 0
except (ValueError, ZeroDivisionError): # 동시에 작성해도 됩니다.
    print("잘못된 입력입니다.") # 잘못된 입력입니다.

# 예외 처리 후 객체를 받아올 수 있습니다.
try:
    result = 10 / 0
except ZeroDivisionError as e: # ZeroDivisionError 예외가 발생하면 그 예외 객체를 e라는 변수에 담으라는 의미입니다.
    print(e) # division by zero

# try-except에는 else도 사용할 수 있으며, else는 예외가 발생하지 않았을 때 실행합니다.
try:
    number = int(input("숫자: "))
except ValueError:
    print("숫자가 아닙니다.")
else:
    print("정상적으로 입력되었습니다.")

# [ finally ]
# finally는 예외 발생 여부와 관계없이 실행된다는 특징을 지니고 있습니다. 예외가 나와도 무조건 실행 !!
try:
    result = 10 / 0
except ZeroDivisionError:
    print("오류 발생") # 오류 발생
finally: # try-except 끝나면 무조건 실행
    print("작업 종료") # 작업 종료

# 그렇다면 finally는 언제 사용될까요?
# 대표적으로 자원 정리(cleanup)에 사용됩니다.
# file = open("test.txt")
# try:
#     data = file.read() # 파일 읽기
# finally: # 파일이 열리고 예외가 발생해도 무조건 실행해서 파일 스트림을 닫으라는 의미입니다.
#     file.close() # 파일 닫기

# [ 예외를 직접 발생시키기 ] - raise
def set_age_first(age):
    if age < 0: # 나이는 음수가 될 수 없으니 예외를 놔줍니다.
        raise ValueError("나이는 음수가 될 수 없습니다.") # Java의 throw와 동일합니다.
    
    print(f"나이: {age}")

try:
    set_age_first(-10)
except ValueError as e:
    print(e)

# [ Exception ]
# Exception은 대부분의 일반적인 실행 오류의 상위 클래스입니다. 모든 일반적인 예외를 잡고 싶을 때 사용합니다.
try:
    num = 10 / 0
except Exception as e:
    print(f"오류 발생: {e}") # 오류 발생: division by zero

# [ 사용자 정의 예외 ]
# 우리가 만든 비즈니스 규칙에 맞는 예외를 정의할 수 있습니다. 실제 서비스에서 굉장히 유용하기 때문에 사용합니다.
# 단순한 Exception보다 예외의 의미가 명확해지기 때문에 많이들 사용자 정의 예외를 통해서 비즈니스 로직을 짜기도 합니다.
# 
# 실무에서 예외 발생 상황을 예상 가능한 실패 상황을 명확하게 분류하고, 적절하게 복구하거나 전달하며, 예상하지 못한 오류는 진단할 수 있도록 만드는 메커니즘으로 다가가야 합니다.
class InvalidAgeError(Exception):
    pass

def set_age_second(age):
    if age < 0:
        raise InvalidAgeError("나이가 잘못되었습니다.")
    
    print(f"나이: {age}")

try:
    set_age_second(-10) # 함수 호출
except InvalidAgeError as e:
    print(e) # 나이가 잘못되었습니다.
