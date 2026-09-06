# [ ChainMap ]
# 여러 개의 딕셔너리를 하나의 논리적인 mapping처럼 묶어서 조회할 수 있습니다.
from collections import ChainMap

defaults = {
    "host": "localhost",
    "port": 8080
}

config = {
    "host": "production.example.com"
}
# 여기서 config가 defaults보다 우선한다고 해봅시다.
settings = ChainMap(config, defaults)

# config에 "host"가 있으니까 그 값을 사용합니다.
print(settings["host"]) # production.example.com

# config에는 "port"가 없기 때문에 defaults에서 찾습니다.
print(settings["port"]) # 8080

# { ChainMap의 조회 순서 }
# ChainMap(config, defaults)이면 config -> 없음? -> defaults -> 없음? -> KeyError 순으로 검색합니다.

# [ 실전에서 어디에 쓸까요? ]
# 설정(configuration)을 여러 단계로 관리할 때 이해하기 좋습니다. (기본 설정 -> 환경 설정 -> 사용자 설정)
default_config = { "timeout": 30, "region": "ap-northeast-2" }
environment_config = { "timeout": 60 }

config = ChainMap(environment_config, default_config)

print(config["timeout"]) # 60
print(config["region"]) # "ap-northeast-2"

# { ChainMap의 중요한 점 }
# ChainMap은 딕셔너리들을 합쳐서 새로운 딕셔너리를 만드는 것과는 다르다는 겁니다.
a = { "x": 1 }
b = { "y": 2 }

# a와 b를 복사해서 하나의 dict를 만든 게 아니고, 원래 딕셔너리를 참조하면서 하나처럼 보여주는 것에 가깝습니다.
c = ChainMap(a, b)

a["x"] = 100
print(c["x"]) # 100
