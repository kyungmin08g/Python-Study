# [ 추상화(Abstraction) ]
# 
# 추상화는 복잡한 내부 구현은 숨기고, 사용자에게 필요한 기능의 규칙이나 인터페이스만 제공하는 것을 의미합니다.
# 추상 클래스의 핵심은 구현이 아니라 규칙입니다. '추상 클래스를 상속하는 클래스는 반드시 method()를 구현해야 한다.'라는 것을 명시해줍니다.
#
# 일종의 Java Inerface와 Abstract와 매우 비슷합니다. (Abstract 관련은 동일합니다.)
# (Java) abstract class = (Python) ABC
# (Java) abstract method = (Python) @abstractmethod

# ABC는 Abstract Base Class의 약자로 추상 기반 클래스 또는 추상 클래스라고 불립니다.
from abc import ABC, abstractmethod

# 추상 클래스
# class Animal(ABC)의 의미는 추상 클래스 기반 클래스라는 것을 명시하는 겁니다. (추상 클래스의 기반을 갖게 되는 것입니다.)
# 하지만 ABC를 상속했다고 해서 무조건 객체 생성을 막는 것은 아닙니다. (진짜 추상 클래스가 아니기 때문입니다.)
class Animal(ABC): # ABC: 추상 클래스의 기반으로 만든다.

    # 추상 메서드
    # @abstractmethod라는 데코레이터는 '이 메서드는 자식 클래스가 반드시 구현해야 한다.'라는 의미를 지니고 있습니다.
    # 구현하지 않았을 때는 아래와 같은 오류를 일으키게 됩니다.
    # TypeError: Can't instantiate abstract class Cat
    # with abstract method sound
    # 
    # 추상 메서드라는 것을 명시하면서 해당 메서드를 하위 클래스에서 구현하지 않을 경우 객체 생성을 하지 못합니다.
    @abstractmethod # @abstractmethod: 자식 클래스가 반드시 구현해야 하는 메서드를 지정한다.
    def sound(self) -> None:
        """동물 울음소리 (하위 클래스가 반드시 구현해야 함)""" # 알려주기 위한 주석
        pass # 이 pass는 왜 쓸까요? 추상 클래스의 목적은 구현이 아닌 규직이기 때문에 상속할 자식한테 구현하라고 넘기는 겁니다.

# 추상 클래스는 직접 객체로 만들 수 없기 때문에 오류가 발생합니다.
# a = Animal()

# 추상화 클래스를 상속 받는 구현체
class Dog(Animal): # 동물의 종류는 많지만 예제이기 때문에 강아지로 선택했습니다.
    # 추상화 클래스의 sound 메서드 구현체 (구현 안 하면 객체 생성 안 됩니다.)
    def sound(self) -> None:
        print("멍멍")

    # Getter로 활용 가능 (단, 정석적인 방법은 아닙니다.)
    get_name = lambda self: self.name
    get_breed = lambda self: self.breed

    # Setter로 활용 가능
    def set_name(self, name) -> None: self.name = name
    def set_breed(self, breed) -> None: self.breed = breed

# 추상 클래스의 메서드를 구현하지 않았을 때 객체 생성이 불가하여 오류가 발생합니다.
# d = Dog()

# Dog 객체 생성
dog = Dog()

# Setter 채우기
dog.set_name("초코")
dog.set_breed("푸들")

# 조회
print(f"이름: {dog.get_name()}") # 초코
print(f"품종: {dog.get_breed()}") # 푸들
dog.sound() # 메서드 호출과 동시에 print("멍멍") 실행
