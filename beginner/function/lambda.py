# [ 람다 함수(Lambda Function) ]

# 이름이 없는 함수로 다음과 같은 형식을 가지며, ruturn 키워드가 붙지 않습니다.
# 형식: lambda parameter: return value
# 람다는 코드를 짧게 만드는 것이 목적이지, 복잡한 함수를 한 줄로 만드는 것이 목적은 아니기 때문에 복잡한 비즈니스 로직이 들어간 함수를 람다로 바꿀 수 없습니다.

# 아래 람다 함수는 일반적인 함수로 풀어보면 다음과 같이 표현할 수 있습니다.
# def add(a, b):
#   return a + b
add_second = lambda a, b: a + b
print(add_second(2, 3)) # 5

# 람다 함수는 이름이 없어 다음과 같이 바로 호출하여 실행할 수 있습니다.
print((lambda x, y: x * y)(7, 6)) # 42

# 조건문과 함께 사용 가능합니다.
check = lambda num: "짝수" if num % 2 == 0 else "홀수"
print(check(9)) # 홀수

# 람다 함수는 한 번만 사용할 간단한 함수를 다른 함수에 전달할 때 사용하는 것이 가장 좋습니다.