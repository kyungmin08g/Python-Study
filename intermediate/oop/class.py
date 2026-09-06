# [ 클래스(Class) ]
# 들어가기 전, 본 필자는 Java/Kotlin을 배운 상태이기 때문에 객체지향의 자세한 내용까지는 작성하지 않겠습니다.

# { 클래스(class)와 객체(object)의 차이 }
# 클래스(class)란 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면이고, 객체(object)란 클래스로 만든 피조물을 의미합니다.
# 이게 사람들이 많이 말하는 객체지향 프로그래밍의 핵심입니다. 이를 기반으로 OOP의 중요 이론인 상속, 다형성 등을 이해할 수 있습니다.
#
# { 객체의 특징 }
# 각 객체마다 고유한 성격을 가집니다. 즉, 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않습니다.
#
# { 객체와 인스턴스의 차이 } - 잘 기억해두셔야 합니다.
# 인스턴스(instance): 클래스로 만든 객체
# a = Cookie()로 만든 a는 객체이며, a 객체는 Cookie의 인스턴스입니다.
# 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용합니다.
# 즉, 정리하자면 객체(object): 실제로 생성된 실체를 일반적으로 부르는 말, 인스턴스(instance): 특정 클래스와의 관계를 강조하는 말

# class 키워드를 사용하여 class를 생성해줍니다.
# 아래 클래스는 계산기 클래스로 계산기에 필요한 기능들을 2~3개정도 구현할 예정입니다.
class Calculator: # Class Name: Calculator
    
    # 클래스 변수는 객체 변수와 달리 클래스로 만든 모든 객체에 공유된다는 특징이 있습니다.
    name = "계산기(Calculator)"

    # 생성자(constructor)
    # __init__() 메서드는 클래스를 초기화할 때 사용합니다.
    def __init__(self) -> None: # 반환 타입은 항상 None입니다.
        self.result = 0 # 결과값

    # 클래스(class)에 함수를 정의하면 메서드(method)라고 불립니다. (함수랑 메서드랑 혼용해서 사용하기도 해서 기억해주시길 바랍니다.)
    # 자신을 인자로 받고 속성을 꺼내어 더해주는 덧셈 메서드
    def plus(self, x: int, y: int) -> int:
        self.result = x + y # 자신의 result 속성에 계산한 값을 대입합니다.
        return self.result # 자신의 result을 반환하면 계산한 값이 반환됩니다.

    # 뺄셈 메서드
    def subtract(self, x: int, y: int) -> int:
        self.result = x - y
        return self.result
    
    # 곱셈 메서드
    def multiply(self, x: int, y: int) -> int:
        self.result = x * y
        return self.result

# Calculator 사용해보기
def calculator() -> None:
    # 객체 생성
    # 객체란 클래스의 완성본을 의미합니다.
    calculator = Calculator()

    # 클래스에 정의되어 있는 메서드들을 사용하여 계산을 해줍니다.
    print(calculator.name) # 계산기(Calculator)
    print(calculator.plus(4, 5)) # 9
    print(calculator.subtract(9, 5)) # 4
    print(calculator.multiply(4, 6)) # 24

calculator() # 함수 호출

# [ pass 명령어 ]
# pass 키워드는 초반에 클래스 배울 때 많이 등장하는 녀셕이며, 아무것도 하지 않고 코드의 자리를 채우는 명령어입니다.
class Pass:
    pass # 아무것도 채우지 못 하면 에디터에서 에러가 나오니까 pass 명령어로 채우겠습니다.

# 자동차 정보에 대한 클래스
class Car:
    # 차 번호와 차 부품 정보를 입력하는 메서드
    def set_part(self, num: str, part: str) -> None: 
        self.num = num
        self.part = part

def info_car():
    car = Car() # 객체 생성
    # set_part 메서드의 첫 번째 매개변수 self에는 set_part 메서드를 호출한 객체 car가 자동으로 전달되기 때문에 첫 번째 매개변수에는 아무것도 넣지 않아도 됩니다.
    car.set_part("1682가23", "gear") # 메서드 호출

    print(f"차 번호: {car.num}, 부품: {car.part}")

info_car()
