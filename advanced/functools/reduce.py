# [ reduce ]
# reduce()는 여러 개의 값을 하나의 값으로 차례차례 누적해서 줄이는 함수입니다.
# 더 정확하게는 reduce()는 iterable의 요소들을 지정된 함수로 누적 결합하여 하나의 값으로 축약하는 함수입니다.
# 
# { reduce()의 구조 }
# 형식: reduce(function, iterable)
# function: 두 값을 어떻게 결합할 것인지 정의, iterable: 처리할 데이터

# { 일반적인 표현 } - 누적 값 구하기
numbers = [1, 2, 3, 4, 5]
result = 0

for number in numbers:
    result += number

print(result) # 15

# { reduce() 함수를 사용한 표현 } - 누적 값 구하기
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)

print(result) # 15

# { 실제 동작 원리 }
# 한 번에 생각하지 말고 두 개씩 처리한다고 생각해봅시다.
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 1 + 2 = 3 + 3 = 6 + 4 = 10 + 5 = 15 즉, 이전 계산 결과가 다음 계산의 입력으로 들어갑니다. (= ((((1 + 2) + 3) + 4) + 5) = 15)
# lambda x, y: x + y 의미: 두 값을 받아서 더하는 함수입니다. 이를 사용하여 reduce()는 이 함수를 계속 호출하는 거죠.
# 따라서 reduce()는 누적해서 하나의 값으로 만드는 과정 자체가 의미 있을 때 유용합니다.

# 곱셈도 가능합니다.
result = reduce(lambda x, y: x * y, numbers)
print(result) # 120
# 즉, reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# 1 * 2 = 2 * 3 = 6 * 4 = 24 * 5 = 120 (= ((((1 × 2) × 3) × 4) × 5) = 120)

# reduce()에는 세 번째 인자로 초기값(initializer)을 넣어줄 수 있습니다.
# 형식: reduce(function, iterable, initializer)
result = reduce(
    lambda x, y: x + y,
    numbers,
    100
)

print(result) # 115
# 초기값 100의 누적값을 더합니다. (= 100 + 15 = 115)

# { reduce()와 map()의 차이 }
result = map(lambda x: x * 2, numbers) # map()은 각각의 값을 변환합니다.
print(result) # [2, 4, 6, 8]
# 하지만 reduce는 하나의 값을 반환하죠. 즉, map()은 여러 개의 값을 반환하고, reduce()는 하나의 값을 반환합니다.

# { filter()와도 비교 }
# filter: 선택하여 여러 개의 값을 반환
result = filter(lambda x: x % 2 == 0, numbers)
print(result) # [2, 4]
