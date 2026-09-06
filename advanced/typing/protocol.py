# [ 프로토콜(Protocol) ]
# Python에서 Protocol이란, 이 객체가 어떤 메서드나 속성을 가지고 있으면, 특정 역할을 할 수 있다고 약속하는 규칙을 말합니다.
# 어떠한 클래스를 상속 받지는 않았지만 구조적으로 동일한다면 필요한 행동을 지니고 있다고 판단합니다. -> 이게 바로 Python에서 말하는 Protocol의 핵심적인 사고방식입니다.
# 
# 일반적으로 클래스는 상속관계를 확인합니다. 하지만 Protocol은 명시적인 관계가 존재하는지를 확인합니다. (ex. Storage 역할을 수행하는 데 필요한 행동을 가지고 있느냐?)
# 처음 배울 때 진짜 헷갈리는 것이 덕 타이핑이랑 프로토콜이랑 도대체 무슨 차이인지 헷갈리는 경우가 많이 있습니다.
# Protocol은 타입 관점에서 코드를 봐야 하고, 덕 타이핑은 필요한 메서드를 가지고 있으면 그냥 사용한다는 관점으로 봐야 합니다.
# 특정 구조를 만족하는지 안 하는지를 봐야 한다는 거죠.
# 덕 타이핑은 그냥 동인한 구조가 아니라 동일한 메소드가 있으면 그것을 덕 타이핑이라고 하고, Protocol은 특정 구조가 만족될 때를 Protocol이라고 합니다. (중요 !!)
# 
# Protocol / Structural Subtyping은 Storage를 중심으로 비유해서 설명해보겠습니다. (이해하기 쉬움)
from typing import Protocol

# 예를 들어서 프로그램에서 저장소(Storage)가 필요하다고 해봅시다. 
# 저장소라면 최소한 아래 기능이 필요하다고 정할 수 있습니다.
class Storage(Protocol):
    def save(self, data: str) -> None:
        pass

    def load(self) -> str:
        return ""
# 여기서 Protocol은 실제 저장소를 구현하는 클래스가 아니라, 'Storage 역할을 하려면 save()와 load()를 제공해야 한다.'라는 규칙을 정의한 것입니다.

# FileStorage - FileStorage는 Storage를 상속하지 않았습니다. 
class FileStorage:
    def save(self, data: str) -> None:
        print(f"파일에 저장: {data}")

    def load(self) -> str:
        return "(파일 데이터)"

# DatabaseStorage - DatabaseStorage도 Storage를 상속하지 않았습니다.
class DatabaseStorage:
    def save(self, data: str) -> None:
        print(f"DB에 저장: {data}")

    def load(self) -> str:
        return "(DB 데이터)"

# 둘 다 Storage라는 클래스를 상속 받지는 않았지만 같은 기능을 하는 두 개의 메소드(save(), load())가 있습니다.
# 그 말은 즉, Storage 역할이 가능하다는 의미를 말합니다. = 구조적으로 Storage의 조건을 만족

def process(storage: Storage):
    storage.save("hello")
    print(storage.load())

# 각 객체를 생성해줍니다.
file_storage = FileStorage()
database_storage = DatabaseStorage()

# Storage 클래스를 상속 하지 않은 각각의 클래스를 process() 함수의 인자로 담습니다.
process(file_storage) # 파일에 저장: hello (파일 데이터)
process(database_storage) # DB에 저장: hello (DB 데이터)

# Storage 입장에서는 중요한 것이 FileStorage인가?, DatabaseStorage인가?가 아닙니다.
# save()가 있는가?, load()가 있는가?가를 봅니다. 그것이 바로 이게 바로 Structural Subtyping입니다.
# 즉, Structural Subtyping는 이름이나 상속 관계가 아니라, 필요한 구조를 갖추고 있느냐를 기준으로 타입을 판단합니다.

# [ 최종 정리 ]
# 덕 타이핑: 필요한 행동을 하면 사용
# Protocol: 필요한 행동을 타입으로 명시
# Structural Subtyping: 그 구조를 갖춘 타입이면 Protocol을 만족
