# [ Literal ]
# Literal은 특정 값만 허용하도록 타입을 제한하는 기능을 제공합니다.

from typing import Literal

def set_mode(mode: Literal["dev", "prod"]):
    pass

set_mode("dev") # OK
set_mode("prod") # OK
# set_mode("test") # 타입 검사에서 오류

# { 일반적인 str과의 차이점 }
# mode: str: 어떤 문자열이든 가능
# mode: Literal["dev", "prod"]: "dev" 또는 "prod"만 가능
# 즉, 이 타입 중에서도 특정 값만 허용한다는 것을 엄격하게 제한할 때 쓰입니다.
