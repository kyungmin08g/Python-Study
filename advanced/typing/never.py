# [ Never ]
# Never은 정상적으로 반환되는 값이 절대 존재하지 않는 경우를 표현합니다.

from typing import Never

# 해당 함수는 절대 정상적으로 return하지 않습니다.
def terminate() -> Never:
    raise RuntimeError("Fatal error")

# 항상 예외가 발생합니다.
def fail(message: str) -> Never:
    raise Exception(message)

# 즉, Any와 정반대입니다. 
# Any: 무엇이든 가능, Never: 아무것도 가능하지 않음
# 정확하게는 Never는 도달할 수 없는 반환 상태를 타입 시스템에 표현하는 용도입니다.
