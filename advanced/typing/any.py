# [ Any ]
# 어떤 타입이든 허용한다는 의미를 가진 타입입니다.
# 정말 타입을 알 수 없거나 타입 검사를 의도적으로 우회해야 할 때 사용합니다.

from typing import Any

data: Any = 10
data = "hello"
data = [1, 2, 3]
data = {"key": "value"}
# Any는 타입 검사기에게 "이건 타입 검사하지 마."라고 하는 것과 동일합니다.
# 하지만 def process(data: Any): ...
# 위 예시와 같이 너무 많이 사용해버리면 data가 뭔지 타입 시스템이 거의 알 수 없게 되어 Type Hint의 의미가 사라집니다.