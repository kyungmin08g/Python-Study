# [ 정적 메서드(Static method) ]
# 정적 메서드는 인스턴스와 클래스의 상태를 사용하지 않는 메서드입니다. (= 인스턴스(self)나 클래스(cls)의 상태에 의존하지 않는 기능을 클래스 내부에 묶어 표현하는 메서드)
# 
# 일반 메서드는 self를 받고, 클래스 메서드는 cls를 받습니다. 하지만 정적 메서드는 아무런 매개변수 없이 동작이 가능합니다. (self, cls 없어도 된다는 의미이며, 어떠한 객체 정보를 필요하지 않다는 것입니다.)
#
# { 질문 }: @staticmethod는 왜 클래스 안에 넣을까? 그냥 일반 함수로 만들면 되는 거 아닌가?
# 그런데 함수가 Calculator와 논리적으로 관련된 기능이라면 클래스 안에 넣어 의미를 묶어줄 수 있기 때문입니다.
# 정적 메서드를 사용하는 목적 중 하나는 인스턴스나 클래스의 상태를 사용하지 않는 기능을 해당 클래스와 논리적으로 묶어두는 것입니다.

# { 예제 }
class Calculator:

    # 
    @staticmethod
    # 인자 2개를 받고 덧셈 연산을 해주는 메서드입니다.
    def plus(a, b): # 말한대로 객체의 데이터를 받지 않습니다. (self, cls 필요없음)
        return a + b

    # 인자 2개를 받고 곱셈 연산을 해주는 메서드입니다.
    @staticmethod
    def multiply(a, b):
        return a * b

c = Calculator() # Calculator 객체 생성
# 객체를 사용하여 정적 메서드 호출
print(f"(object) 5 + 6 = {c.plus(5,6)}") # 11
print(f"(object) 5 x 6 = {c.multiply(5,6)}") # 30

# 클래스를 사용하여 정적 메서드 호출
print(f"(class) 5 + 6 = {Calculator.plus(5, 6)}") # 11
print(f"(class) 5 x 6 = {Calculator.multiply(5, 6)}") # 30
# 호출할 때 보통 위와 같이 클래스를 통해 호출합니다.
