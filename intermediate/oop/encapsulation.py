# [ 캡슐화(Encapsulation) ]
# 캡슐화란 객체의 내부 상태와 구현 방법을 외부로부터 감추고, 필요한 기능만 외부에 제공하는 것을 의미합니다.
# 캡슐화는 데이터를 보호만 하는 것이 아니라 객체의 상태와 동작을 하나의 단위로 묶고, 외부가 내부 구현에 직접 의존하지 않도록 하는 것이 중요 포인트입니다.
# 정리하자면 캡슐화는 객체의 내부 상태와 구현을 외부로부터 감추고, 객체가 제공하는 적절한 인터페이스를 통해서만 객체와 상호작용하도록 만드는 설계 원칙입니다.

# Python의 접근 제어 방식
# 1. public = self.hp (공개(외부에서 접근 가능))
# 2. protected = self._hp (자신이나 상속받은 자식 클래스에서만 사용하라는 개발자 간의 관행(약속))
# 3. private = self.__hp (비공개(외부에서 직접 접근할 수 없음))
# 
# 위와 같이 밑줄을 이용하면 Python이 이름 맹글링(Name Mangling)을 적용해줍니다.
# Python의 철학은 Java처럼 강력하게 접근을 차단하기보다는 개발자가 명확한 의도를 표현하고 그 규칙을 따르는 방식에 가깝기 때문에 외부에서 호출할 수 있지만 개발자 관례라고 보면 될 것 같습니다. (지키는게 가장 좋겠죠)
# 

# 그렇다면 왜 캡슐화를 할까요? 왜 내부 데이터를 숨겨야 할까요?
# 아래 코드로 예를 들어보겠습니다.
class Player:
    # __init__은 private이 아닙니다! 헷갈릴만 하지만 private은 앞에 밑줄(_) 2개가 들어갑니다. ex. __name
    # __init__은 매직 메서드라고 불리며, 시스템이 특정 상황에 자동으로 호출하는 공개(Public) 메서드입니다. 외부에서 직접 호출할 수도 있으며, 이름 맹글링(Name Mangling)이 일어나지 않습니다.
    def __init__(self) -> None:
        # 플레이어의 체력에는 규칙이 있다고 해봅시다.
        # -> HP는 0보다 작을 수 없으며, 최대 100
        # self.hp = 100 # public 접근
        # self._hp = 100 # protected 접근
        self.__hp: int = 100 # private 접근

    # Python에서는 getter를 만들 때 @property 데코레이터를 사용합니다. (다른 언어와 차별점)
    # @property는 getter를 만들기 위한 데코레이터입니다. 
    # 해당 데코레이터를 사용하지 않고서 구현 가능하지만 명시적으로 getter의 역할을 만드는 것이 캡슐화 목적에도 맞다고 생각합니다.
    # @property를 사용함으로써 캡슐화에 맞는 setter도 구현 가능합니다.
    @property
    def hp(self) -> int:
        return self.__hp

    # 처음 공부할 때 저는 실수를 했었습니다.
    # @set_hp.setter
    # def set_hp(slef, hp) -> None:
    # 위와 같이 코드를 작성한다면 분명 에러가 날 것입니다. 왜냐하면 우리가 만들어준 getter의 setter를 만드는 것이라 그렇습니다.
    # setter를 만들 때는 getter의 이름을 따라갑니다.
    # ex. get_hp라는 getter가 있다면 setter는 @get_hp.setter 이런식으로 만들어야 합니다. 근데 이름을 좀 신경 써서 get을 안 붙히는게 좋을 듯합니다.
    @hp.setter
    def hp(slef, hp) -> None: # 메서드 이름은 위 주석과 상관 없습니다. (동일하는게 마음이 편하여 그렇게 진행하였습니다.)
        if hp < 0:
            raise ValueError("체력은 음수가 될 수 없습니다.")
        slef.__hp = hp

    def take_damage(self, damage) -> None:
        self.__hp -= damage

        if self.__hp < 0:
            self.__hp = 0
        
        print(f"(class) Player HP: {self.__hp}")

    def heal(self, amount) -> None:
        self.__hp += amount

        if self.__hp > 100:
            self.__hp = 100
        
        print(f"(class) Player HP: {self.__hp}")

# player 객체를 생성하고 아래와 같이 hp를 수정하면 어떻게 될까요? 우리가 정한 HP의 규칙이 사라집니다.
# 이처럼 이런 실수를 방지하고자 이름 맹글링(Name Mangling) 방식으로 캡슐화를 수행할 수 있습니다.
player = Player()
# player.hp = -500
# player.hp = 999999

player.take_damage(30) # 70 
player.heal(10) # 80

# 이런식으로 이름 맹글링(Name Mangling)을 사용해도 개발자간 관례이기 때문에 언어 차원에서는 정상적으로 동작합니다.
# 개발자 입장에서는 허용하지 않지만 접근이 가능해지는 것은 허용되지 않아야 한다고 생각합니다. 그렇기 때문에 본 필자는 이름 맹글링(Name Mangling) 방식을 꼭 사용하는게 좋을 것 같다고 판단합니다.
# player.__hp = 20
# print(player.__hp)

# getter/setter 사용
print(f"(outside) Player HP: {player.hp}") # getter가 동작하며, 출력으로 80을 출력합니다.
player.hp = 30 # setter 동작
print(f"(outside) Player HP: {player.hp}") # 30

# 필자의 개인적인 생각은 _ or __은 사용하는 것이 비즈니스 로직을 설계하는데 좋아보입니다.
