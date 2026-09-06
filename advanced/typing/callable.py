# [ Callable ]
# Callable은 함수 타입을 표현할 때 사용합니다.
# 형식: Callable[[매개변수 타입], 반환 타입]

from typing import Callable

# Callable[[int], str]: int를 받아서 str을 반환하는 함수라는 의미를 지닙니다. (타입을 Python 수준에서 엄격하게 다룰 때 좋을 듯합니다.)
def execute(func: Callable[[int], str], value: int) -> str:
    return func(value)

# { 예시 }
def convert(x: int) -> str:
    return str(x)

print(type(execute(convert, 10))) # <class 'str'>

# [ 최종 정리 ]
# Callable[[str, int], bool] -> str, int를 받아서 bool을 반환하는 함수.
# 함수 자체를 타입으로 표현할 때 사용합니다.