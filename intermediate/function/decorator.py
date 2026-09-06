# [ 데코레이터(Decorator) ]

# 기존 함수 코드를 직접 수정하지 않고도 실행 전후에 새로운 기능을 더해주는 확장 도구로 불리며, 기존 함수를 수정하지 않고, 함수에 기능을 추가하는 방법입니다.
# 내부적으로는 함수를 다른 함수에게 전달하고, 새로운 함수를 반환하는 구조를 사용합니다.
# 고차 함수를 배웠다면 데코레이터는 고차 함수를 기반으로 만들어졌다는 사실을 깨달았을 겁니다.
# 또한, Spring의 AOP와 비슷한 기능을 합니다. (완전 동일 X)

# 내부 함수인 wrapper를 상위 함수의 반환 값으로 되어 있기 때문에 중첩 함수이며, 고차 함수입니다. (클로저 X, 고차 함수 O)
def decorator(func): # 함수의 매개변수로 함수를 받습니다.
    def wrapper(): # wrapper라는 이름은 감싸는 함수라고 표현하고 싶었기 때문에 wrapper라고 작성하였습니다. (일반적으로 wrapper라고 부르기도 합니다.)
        print("함수 실행 전")
        func() # 대상 함수를 실행합니다.
        print("함수 실행 후")

    return wrapper

@decorator # hello 함수가 decorator 함수의 인자가 됩니다. (decorator의 대상 함수)
def hello():
    print("(decorator) Hello, Python!")
hello() # 함수 호출하여 실행

# 문제. 함수 실행 시간 측정하기
import time

def elapsed_time(func):
    def wrapper():
        start_time = time.time() # 시작 시간 기록
        func() # 대상 함수 실행 시작
        end_time = time.time() # 종료 시간 기록

        print(f"실행 시간: {end_time - start_time:.2f}초")
    return wrapper

@elapsed_time
def main_hello():
    print("main_hello 함수 실행")
    time.sleep(5) # 예를 들어 5초 정도 딜레이가 있다고 만듦
main_hello() # 함수 호출하여 실행 시간 측정