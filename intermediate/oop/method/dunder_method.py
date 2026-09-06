# [ 매직 메서드(dunder(double underscore) method) ]
# 
# 매직 메서드는 이름이 __로 시작하고 __로 끝나는 메서드를 말합니다. 
# 이들은 이미 파이썬 내에 정의되어 있고, 클래스 내부에서 매직 메소드들을 오버라이딩 하여 사용할 수 있습니다. 
# 또한 직접 호출해서 사용하지 않고, 정해진 규칙에 따라 알아서 호출된다는 특징이 있으며, 앞 뒤로 언더바가 두 개씩 붙습니다.
# 
# { 주요 매직 메서드 }
# __init__: 객체가 생성될 때 호출되는 초기화 메서드(생성자)입니다. 객체의 초기 속성(변수)을 설정할 때 사용합니다.
# __str__: 객체를 print()하거나 str() 함수로 변환할 때 호출되는 사용자 친화적 문자열 표현입니다. 사람이 읽기 좋은 형태로 정보를 반환합니다.
# __repr__: 객체의 공식적인 문자열 표현입니다. 주로 디버깅이나 개발자 도구(REPL)에서 객체가 어떻게 생성되었는지 명확하게 식별할 수 있는 정보를 반환합니다.
# __len__: 객체의 길이를 반환하는 메서드로, 내장 함수 len()을 호출할 때 내부적으로 실행됩니다.
# __eq__: 동등성 비교 연산자 ==를 사용할 때 호출됩니다. 두 객체의 값이 같은지 여부를 정합니다.
# __lt__: 미만(Less Than) 비교 연산자 <를 사용할 때 호출됩니다. 정렬(sort()) 기능을 구현할 때 필수적으로 쓰입니다.
# __add__: 더하기 연산자 +를 사용할 때 호출됩니다. 객체와 객체를 더했을 때의 행동을 정의합니다.
# __getitem__: 객체에 인덱스나 키를 통해 접근할 때(object[key]) 호출됩니다. 리스트나 딕셔너리처럼 대괄호([]) 문법을 클래스에 구현할 때 씁니다.
#
#
# { 왜 필요할까요? }
# 매직 메서드(dunder method)는 Python의 특정 문법이나 연산이 객체에서 어떻게 동작할지를 정의하는 역할을 합니다.

# { 진짜 간단한 예제 }
message = "Hello"
print(len(message)) # 이 메서드를 호출하면 message.__len__() 매직 메서드가 자동으로 호출됩니다. (출력: 5)
# def __len__(self) -> int: ...

# { 예제 }
class Person:
    # 기본 생성자 (= 매직 매서드)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 사용자가 보기 좋은 문자열을 만드는 매직 메서드
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"
    
    # 개발자가 객체의 상태를 파악하기 좋게 표현한 매직 메서드 (= Java의 toString()과 동일)
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"
    # { !r }
    # 파이썬 내장 함수 repr()을 호출하여 객체의 공식적인(string representation) 문자열로 변환하라는 뜻입니다.
    # f"{variable!r}" 형태로 사용하며, 일반 문자열과 달리 따옴표('...')나 특수 기호가 포함된 객체의 원래 형태를 살려서 보여줄 때 씁니다.

person = Person("Kim", 20) # 객체 생성
print(repr(person)) # person 객체를 그대로 출력하면 매직 메서드 __str__()이 호출되어 출력됩니다. (출력: 이름: Kim, 나이: 20)

# { 매직 메서드들 구현 예제 }
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"[상품] {self.name}"

    def __repr__(self):
        return f"Item(name={self.name!r}, price={self.price!r})"

    def __len__(self):
        return len(self.name) # 예시로 상품명 글자 수를 길이로 정의

    def __eq__(self, other):
        return self.price == other.price # 가격이 같으면 같은 상품으로 취급

    def __lt__(self, other):
        return self.price < other.price # 가격 기준 정렬용

    def __add__(self, other):
        return self.price + other.price # 두 상품을 더하면 가격의 합을 반환

    def __getitem__(self, index):
        # 인덱스 0은 이름, 1은 가격을 반환하도록 설정
        if index == 0: return self.name
        elif index == 1: return self.price
        raise IndexError


# 1. __init__, __str__, __repr__ 작동
item1 = Item("키보드", 50000)
item2 = Item("마우스", 30000)

print(item1) # __str__ 호출 (출력: [상품] 키보드)
print(repr(item1)) # __repr__ 호출 (출력: Item(name='키보드', price=50000))

# 2. __len__, __getitem__ 작동
print(len(item1)) # __len__ 호출 (출력: 3 (글자 수))
print(item1[0]) # __getitem__ 호출 (출력: 키보드)

# 3. __eq__, __lt__, __add__ 작동
print(item1 == item2) # __eq__ 호출 (출력: False)
print(item1 > item2) # __lt__ 호출 (출력: True (item2 < item1 이므로))
print(item1 + item2) # __add__ 호출 (출력: 80000)
