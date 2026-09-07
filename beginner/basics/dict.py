# 딕셔너리(dict) (= Java의 HashMap)
from typing import Any # 모든 타입 허용을 위해 Any를 import 합니다.

# 딕셔너리는 key-value 쌍 형식으로 데이터를 저장합니다. key는 중복될 수 없으며, value는 중복될 수 있습니다.
dict_data_first: dict[int, str] = { 1: "Hello", 2: "World", }

print(f"dict: {dict_data_first}") # (terminal print: dict: {1: 'Hello', 2: 'World'})
print(f"dict[1]: {dict_data_first[1]}") # (terminal print: dict[1]: Hello)

# [ 값 복사하여 새로운 key-value 쌍 추가 ]
dict_data_first.copy() # dict_data_first의 값 자체를 복사합니다. (주소값이 아닌, 값 자체를 복사합니다.)
dict_data_first[3] = "Python" # dict_data_first에 새로운 key-value 쌍을 추가합니다.

print(f"dict: {dict_data_first}") # (terminal print: dict: {1: 'Hello', 2: 'World', 3: 'Python'})

# 딕셔너리의 value는 모든 타입 허용을 위해 Any를 사용합니다.
# 딕셔너리 타입을 선언하지 않고 타입 유추로 선언할 수도 있습니다.
dict_data_second: dict[int, Any] = { 1: "Kyungmin", 2: 30, }

print(f"dict: {dict_data_second}") # (terminal print: dict: {1: 'Kyungmin', 2: 30})

# { 여러가지 타입 삽입 }
# value에 list, tuple, dict 등 다양한 타입을 넣을 수 있습니다.
# JSON 형식과 유사합니다. (JSON 형식은 key는 string만 허용하지만, dict는 모든 타입 허용, JSON과 완전 동일 X)
dict_data_third: dict[str, Any] = {
    "name": "Kyungmin",
    "age": 30,
    "hobbies": ["reading", "swimming"],
    "address": {
        "city": "Seoul",
        "country": "South Korea",
    }
}
print(f"dict: {dict_data_third}") # (terminal print: dict: {'name': 'Kyungmin', 'age': 30, 'hobbies': ['reading', 'swimming'], 'address': {'city': 'Seoul', 'country': 'South Korea'}})
print(f"address: {dict_data_third['address']['city']}") # (terminal print: address: Seoul)

# { 딕셔너리 삭제 }
# del는 지정한 Key에 해당하는 key-value 쌍이 삭제되는 키워드입니다.
del dict_data_third["hobbies"] # 딕셔너리에서 key-value 쌍을 삭제합니다. (del 키워드 사용)
print(f"dict: {dict_data_third}") # (terminal print: dict: {'name': 'Kyungmin', 'age': 30, 'address': {'city': 'Seoul', 'country': 'South Korea'}})

# { 해당 Key가 딕셔너리 안에 있는지 조사 }
# name key가 dict_data_third 딕셔너리 안에 있는지 조사합니다.
print(f"{'name' in dict_data_third}") # (terminal print: True)
