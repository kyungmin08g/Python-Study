# [ 상속(Inheritance) ]
# 형식: class Class_name(Superclass_name)
#
# 상속(Inheritance)이란 '물려받다'라는 의미로, '재산을 상속받다'라고 할 때의 상속과 같은 의미입니다.
# 언어 차원에서는 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것을 말합니다.
# 
# 자식 클래스만의 기능도 추가할 수 있으며, 그와 동시에 자식 클래스는 부모의 기능을 사용할 수 있습니다. 또한, 부모의 메서드를 자식이 재정의할 수도 있습니다.
# 상속은 'is-a' 관계를 표현합니다. ex. Cat is an Animal, Car is a Vehicle, Student is a Person

# 부모 클래스(Base Class / Parent Class / Superclass)
class Animal:
    def eat(self):
        print("먹는다")

    def sleep(self):
        print("잔다")

# 자식 클래스(Derived Class / Child Class / Subclass)
# 실제 객체를 만들고 Dog에 접근하게 되면 Animal의 기능을 물려받아 사용 가능합니다.
class Dog(Animal): # Dog 클래스를 만들되, Animal 클래스를 상속받겠다는 의미입니다.
    def bark(self):
        print("멍멍")

class Cat(Animal):
    def meow(self):
        print("야옹")

def animal():
    dog = Dog() # Dog 객체 생성
    dog.sleep() # 부모 클래스의 메서드 (-> 잔다)
    dog.bark() # 멍멍

    cat = Cat() # Cat 객체 생성
    cat.eat() # 부모 클래스의 메서드 (-> 먹는다)
    cat.meow() # 야옹
animal() # 함수 호출

# [ super() ]
# super()는 자식 클래스에서 부모 클래스의 메서드나 초기화 로직을 호출하기 위해 사용하며, 특히 상속에서 부모가 이미 만들어 놓은 코드를 다시 작성하지 않고 재사용하기 위해 많이 사용합니다.
# Dog_2.__init__()
#  ↓
# super().__init__(name)
#  ↓
# Animal_2.__init__(name)
#  ↓
# self.name = name
class Animal_2:
    def __init__(self, name):
        self.name = name

class Dog_2(Animal_2):
    def __init__(self, name, breed):
        # 부모 클래스의 __init__()도 같이 실행해달라는 의미입니다.
        super().__init__(name) # 부모 클래스의 초기화 값을 자식 클래스의 초기값으로 받아 사용하는 코드입니다. name을 참조하면 부모 클래스의 name을 참조하게 되는 것입니다.
        self.breed = breed

def animal_2():
    dog = Dog_2("초코", "푸들")
    print(dog.name) # 초코
    print(dog.breed) # 푸들

animal_2()

# { issubclass() }
# 객체가 아니라 클래스 사이의 상속 관계를 확인하고 싶다면 issubclass()를 사용해주면 bool type으로 나옵니다.
print(issubclass(Dog_2, Animal_2)) # True
