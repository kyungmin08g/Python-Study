# [ defaultdict ]
# defaultdict는 존재하지 않는 키를 조회했을 때, 미리 지정한 기본값을 자동으로 만들어주는 딕셔너리입니다.

# { 일반적인 dict 문제 }
users = {}
# kim라는 key가 없기 때문에 예외를 발생시킵니다.
# print(users["kim"]) # KeyError: 'kim'

# 그래서 이를 해결하기 위해 다음과 같이 작성합니다.
# 키가 있는지 확인하고 없으면 기본값을 넣고, 그 다음 데이터를 추가해야 한다는 것을 코드로 표현한 것입니다.
if "kim" not in users: # users에 "kim"이 없을 경우
    users["kim"] = []

users["kim"].append("AWS")
# 하지만 defaultdict는 위 과정을 줄여줍니다.

# { defaultdict를 쓸 경우 }
from collections import defaultdict

# defaultdict(list): 존재하지 않는 키를 조회하면 list()를 호출해서 빈 리스트를 만들어 달라는 의미입니다.
users = defaultdict(list)
# 키가 없었는데도 자동으로 새로운 리스트가 만들어진 것을 볼 수 있습니다.
print(users["kim"]) # []

users["kim"].append("AWS")
print(users) # defaultdict(<class 'list'>, {'kim': ['AWS']})

# defaultdict(list)가 의미하는 것
# list는 리스트 자체를 넣는 게 아닙니다. 즉, 내부적으로 필요한 순간에 list()를 호출하는 겁니다.
# users["kim"] 해서 kim이 없다면 list()를 호출해서 만들어줍니다.
# 
# defaultdict는 어떤 기본값을 만들 수 있을까요?
# { list }
data = defaultdict(list)

data["aws"].append("EC2")
data["aws"].append("S3")
data["aws"].append("IAM")

print(data["aws"]) # ["EC2", "S3", "IAM"]

# int
counter = defaultdict(int)

counter["apple"] += 1
counter["apple"] += 1
counter["banana"] += 1

print(counter) # defaultdict(<class 'int'>, {'apple': 2, 'banana': 1})

# set
data = defaultdict(set)

data["kim"].add("AWS")
data["kim"].add("Linux")
data["kim"].add("AWS")

# set이기 때문에 중복이 제거됩니다.
print(data) # defaultdict(<class 'set'>, {'kim': {'Linux', 'AWS'}})

# { 실전 예제 }
# IP별로 요청한 API를 묶는다고 해봅시다.
logs = [
    ("10.0.0.1", "/login"),
    ("10.0.0.1", "/users"),
    ("10.0.0.2", "/login"),
    ("10.0.0.1", "/admin"),
    ("10.0.0.2", "/users"),
]

data = defaultdict(list)

for ip, path in logs:
    data[ip].append(path)

print(data) # defaultdict(<class 'list'>, {'10.0.0.1': ['/login', '/users', '/admin'], '10.0.0.2': ['/login', '/users']})
# 이런 그룹화(grouping) 작업에서 defaultdict가 정말 편합니다.

# { Counter와 defaultdict의 관계 }
# Counter: 몇 번 등장했는가?
# defaultdict: 키가 없을 때 어떤 기본값을 만들어줄 것인가?

# dict -> 키가 없으면 KeyError
# defaultdict(list) -> 키가 없으면 []
# defaultdict(int) -> 키가 없으면 0
# defaultdict(set) -> 키가 없으면 set()

# { 최종 정리 }
# defaultdict의 본질은 없는 키를 만났을 때 default_factory를 호출해서 기본값을 만들어주는 딕셔너리라고 이해하면 정확합니다.
