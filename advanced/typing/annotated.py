# [ Annotated ]
# 타입에 추가적인 메타데이터(metadata)를 붙이는 기능입니다.
# 이 값은 int 타입인데, 여기에 추가 설명/정보도 같이 붙여두자라는 용도로 많이 쓰이죠.
# 이 값이 어떤 의미와 제약을 가지고 있는지 표현하기 좋습니다.

from typing import Annotated

# 형식: Annotated[타입, 메타데이터]
# int가 실제 타입이고, "사용자의 나이"가 추가 정보(metadata)입니다.
age: Annotated[int, "사용자의 나이"]

# { 왜 필요할까요? } - 예시
# port는 int이고, 추가적으로 "1~65535"라는 의미를 붙여놓았다는 의미가 됩니다.
# 하지만 Annotated 자체가 1~65535인지 검사해주는 것은 아닙니다.
# 아래와 같이 작성해도 Python 자체가 자동으로 오류를 발생시키지는 않습니다.
port: Annotated[int, "1~65535"]
port = 99999

# Annotated는 정보를 붙이는 역할이고, 그 정보를 실제로 해석해서 검증하는 것은 별도의 도구나 프레임워크가 담당할 수 있습니다. (= Annotated = 정보를 붙이는 역할)
port: Annotated[int, "1~65535"]
