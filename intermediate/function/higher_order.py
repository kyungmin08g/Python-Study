# [ 고차 함수(Higher-Order Function) ]
# 함수를 인자로 받거나, 함수를 반환하는 함수입니다.

def add(a, b): # 매개변수 a, b를 받고 더해주는 함수
    return a + b

# calculate() 함수 인자로는 function, a, b가 담길 수 있습니다. 또한, 반환 값으로는 함수로 받은 매개변수로 반환합니다. 
# 즉, 함수의 인자를 함수로 받으며, 함수를 반환 값으로 사용한다는 점에서 고차 함수라고 할 수 있습니다.
def calculate(func, a, b):
    return func(a, b) # 매개변수로 받은 함수 반환

# Python에서는 함수도 결국 객체(Object)입니다.
# add는 객체 그 자체를 의미하며, add() 함수를 호출하는 구조와 완전히 다릅니다.
result = calculate(add, 10, 20) # calculate() 함수 호출과 동시에 반환할 때 add() 함수를 호출합니다.
print(result) # 30