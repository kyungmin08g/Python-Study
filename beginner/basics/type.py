# [ 문자열(str) ] - 문자나 문자열을 표현할 때 쓰입니다.
name: str = "Kyungmin Kim"
print(f"name: {name}") # name: Kyungmin Kim
print(name is "Kyungmin") # False

# [ 숫자(int) ] - 정수형을 표현할 때 쓰입니다.
age: int = 20
print(f"age: {age}") # age: 20

# [ 부동소수점(float) ] - 소수점을 표현할 때 쓰입니다. (Python에는 double 타입이 없습니다.)
weight: float = 65.3
print(f"weight: {weight}") # weight: 65.3

# [ 배열(list) ] - 변경 가능한 배열을 필요로 할 때 쓰입니다. (mutable)
array_data: list[int] = [1, 2, 3, 4, 5]
print(f"array: {array_data[0]} (변경 전)") # 1
array_data[0] = 100
print(f"array: {array_data[0]} (변경 후)") # 100

# [ 튜플(tuple) ] - 변경할 수 없는 배열을 필요로 할 때 쓰입니다. (immutable)
tuple_data: tuple[int, str, bool] = (1, "Hello", True) # 튜플은 배열과 달리 요소를 변경할 수 없습니다. 외에는 다 list 역할과 동일합니다.
print(f"tuple: {tuple_data}")

# [ 불(bool) ] - 참과 거짓을 표현할 때 쓰입니다. (True, False)
is_active_first: bool = True
is_active_second: bool = False
print(f"is_active_first: {is_active_first}, is_active_second: {is_active_second}") # is_active_first: True, is_active_second: False

# [ None ] - 값이 없음을 표현할 때 쓰입니다.
nothing = None
print(f"nothing: {nothing}") # nothing: None