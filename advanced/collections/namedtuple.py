# [ namedtuple ]
# namedtuple은 튜플의 각 요소에 이름을 붙여주는 자료구조입니다.
from collections import namedtuple

# namedtuple은 기본적으로 튜플입니다.
# 즉, namedtuple = 이름을 가진 필드를 추가한 tuple이라고 생각하면 됩니다. 이로써 가독성이 좋아지는 장점을 가집니다.

# 중요한 것은 namedtuple은 immutable이다는 점입니다.
# 애초에 튜플이기 때문에 값을 변경할 수 없습니다. 따라서 간단한 읽기 전용 데이터 구조에 적합합니다. (= @dataclass와 비슷한 구조를 가집니다.)
# 단, namedtuple은 알아둘 가치가 있지만, 현대 Python에서는 dataclass가 더 자주 사용되는 경우가 많습니다.
User = namedtuple("User", ["name", "age", "role"])
user = User("kim", 20, "admin")

# user.name = "lee" # 변경 불가 (실행 시 AttributeError 예외가 발생됩니다.)

print(user) # User(name='kim', age=20, role='admin')
print(user.name) # kim
print(user.age) # 20
print(user.role) # admin