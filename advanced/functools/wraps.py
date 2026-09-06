# [ wraps ]
# wraps는 데코레이터를 만들 때 거의 필수적으로 사용하는 도구로, 데코레이터가 원본 함수의 정보를 유지하도록 해주는 도구입니다.

# 질문. 데코레이터를 만들면 무슨 일이 생길까요? 
# 간단한 예제를 통해 알아보겠습니다.
import time

# 특정 함수 실행 시간 측정 데코레이터
def timer(func):
    def wrapper():
        start_time = time.time()
        func() # 특정 함수 호출하여 실행
        end_time = time.time()

        print(f"실행시간: {end_time - start_time:.2f}초")
    
    return wrapper

@timer # (= hello = timer(hello))
def hello():
    """인사를 출력하는 함수""" # __doc__ 함수로 metadata 확인 가능
    return "Hello"

print(hello.__name__) # wrapper
print(hello.__doc__) # None
# 위와 같이 __name__와 __doc__ 매직 메소드를 사용하면 hello, "인사를 출력하는 함수" 나와야 하는 것이 정상이지만 wrapper, None으로 나옵니다.
# 원래 함수 이름은 hello였는데 wrapper가 되어버렸습니다. 왜 그렇게 나올까요? 
# 원래 hello -> timer(hello) -> wrapper 반환 -> hello = wrapper 즉, hello라는 이름이 실제로는 wrapper 함수를 가리키게 됩니다.
# 이런 문제를 해결하기 위해 metadata 보존을 위한 도구가 바로 @wraps(func) 데코레이터입니다.
# 
# wraps 사용 예제
from functools import wraps

# @wraps를 사용한 특정 함수 실행 시간 특정 데코레이터
def wraps_timer(func):

    @wraps(func) # wrapper는 func를 감싼 함수이기 때문에 func의 중요한 metadata를 wrapper에 복사해달라고 합니다. (원본 함수의 metadata 손실 없음)
    def wrapper():
        start_time = time.time()
        func() # 특정 함수 호출하여 실행
        end_time = time.time()

        print(f"실행시간: {end_time - start_time:.2f}초")

    return wrapper

# @wraps를 사용한 데코레이터 사용
@wraps_timer
def wraps_hello(): # __name__에서 원본 함수의 이름 확인 가능
    """인사를 출력하는 함수""" # __doc__에서 원본 함수의 문서 확인 가능
    return "Hello"

print(wraps_hello.__wrapped__) # <function wraps_hello at 0x1098c6980>
print(wraps_hello.__name__) # wraps_hello
print(wraps_hello.__doc__) # 인사를 출력하는 함수
# 출력 시 원본 함수의 정보가 유지된다는 것을 알 수 있습니다.
# 
# wraps는 정확히 무엇을 할까요?
# wrapper는 func를 감싼 함수이기 때문에 func의 중요한 metadata를 wrapper에 복사해달라는 의미로 동작하게 됩니다.
# 대표적으로 원본 함수의 __name__, __qualname__, __doc__, __module__, __annotations__와 같은 정보를 유지하는 데 도움을 줍니다.
# 즉, 원본 함수와 wrapper에게 전부 metadata가 있는 셈이죠.

# 그렇다면 이번에는 wraps의 정체를 파헤쳐봅시다.
# wraps가 무엇인지 알았으니 그 내부 원리를 봐봅시다.
# @wraps(func)
# def wrapper(): ...
# 사실 위 코드는 wrapper = wraps(func)(wrapper) 이 코드를 내부적으로 실행합니다.
# 즉, @wraps(func)는 내부적으로 update_wrapper()를 이용합니다.
# @wraps(func) -> wrapper에 func의 메타데이터를 적용하는 함수 반환 -> wrapper에 메타데이터 복사
# 
# @wraps(func)에 내부 구현을 보면 반환 값이 다음과 같습니다.
# return partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)
# 결국 update_wrapper를 사용합니다.
# 
from functools import update_wrapper # 사실 update_wrapper 함수가 따로 있습니다.
# 
# update_wrapper를 사용하여 @wraps(func)를 구현해보겠습니다.
def decorator(func):
    def wrapper():
        return func()

    update_wrapper(wrapper, func)

    return wrapper
# 자 이렇게 보니까 어떤가요? update_wrapper(wrapper, func) 이렇게 함수를 호출하는 것보다 데코레이터로 선언해주는 게 더 편하지 않나요?
# 그런 이유 때문에 @wraps(func)이 더 많이 사용하기도 하며, 함수 정보를 조사하는 도구에서 문제가 생길 수 있기 때문에 해당 도구를 사용합니다. 
# (metadata가 필요하지 않을 때는 모르겠지만 필요로 할 때는 유용하게 사용할 것 같습니다.)

# [ 최종 정리 ]
# - 데코레이터: 원본 함수를 wrapper가 대신하게 됨 (생길 수 있는 문제: 함수 이름/문서 등의 metadata가 wrapper 기준으로 바뀔 수 있음)
# - @wraps(func): wrapper가 원본 함수의 metadata를 유지하도록 함
# 내부 동작 원리: @wraps(func) 호출 시 -> update_wrapper() 실행 -> 원본 함수의 metadata를 wrapper에 적용
