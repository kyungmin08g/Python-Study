# [ 클래스 메서드(Class method) ]
# 클래스 메서드는 인스턴스가 아니라 클래스 자체를 대상으로 동작하는 메서드입니다. (= 클래스 자체를 대상으로 동작하며, 첫 번째 인자로 클래스 객체를 받는 메서드)
# 
# { 알아둬야 할 이론 }
# 인스턴스 메서드: self -> 인스턴스
# 클래스 메서드: cls -> 클래스
# 즉, self는 인스턴스를 의미하며, cls는 클래스 자체를 의미합니다.

# { 언제 사용해야 할까요? }
# 클래스 변수를 다룰 때, 클래스 자체의 상태를 변경할 때, 대체 생성자를 만들 때 사용하면 됩니다.

# { 예제 }
# 상위 클래스 - Payment
class Payment:
    amount = 0

    # 매개변수 cls는 class의 약자이며, @classmethod는 해당 메서드를 클래스 메서드로 취급하도록 만들어 주는 데코레이터입니다.
    @classmethod
    def pay(cls) -> None:
        print(cls.amount)
        
# 하위 클래스 - TossPayment
class TossPayment(Payment):
    amount = 100

# cls가 Payment를 가리키기 때문에 cls를 사용하면 현재 호출한 클래스에 맞게 동작할 수 있습니다.
# 객체 생성이 아닌 클래스의 대한 메서드 초훌 (Payment() X, Payment O)
Payment.pay()

# [ 대체 생성자(Alternative constructor) ]
# @classmethod는 대표적으로 대체 생성자에 가장 많이 사용됩니다.

# { 예제 }
class User:
    # 기본 생성자
    def __init__(self, user_id: int, name: str, age: int, mail: str) -> None:
        self.user_id = user_id
        self.name = name
        self.age = age
        self.mail = mail

    # 대체(보조) 생성자
    # 여기서는 mail을 받지 않습니다.
    @classmethod
    def init(cls, user_id: int, name: str, age: int) -> User:
        return cls(user_id, name, age, "")

    @property
    def get_id(self) -> int:
        return self.user_id

    @property
    def get_name(self) -> str:
        return self.name

user = User.init(1, "Kyungmin Kim", 20)
print(f"user id: {user.get_id}, user name: {user.get_name}")
