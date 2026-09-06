# [ TypedDict ]
# TypedDict는 딕셔너리의 구조에 타입을 지정하는 것입니다.
# dict의 키와 값 구조를 타입으로 정의합니다.

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

# user: User = {
#     "name": "Kim",
#     "age": "20" # 타입 오류
# }
user: User = {
    "name": "Kyungmin",
    "age": 20
}

# { 이것이 왜 유용할까요? }
# 바로 API 응답이나 JSON처럼 딕셔너리 형태의 데이터 구조를 명확하게 표현할 수 있기 때문입니다.