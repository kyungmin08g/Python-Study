# [ 패키지(Package) ]
# 패키지(Package)는 관련된 Module들을 디렉터리 단위로 묶어서 관리하는 구조를 의미합니다. 즉, 패키지는 폴더와 동일한 기능을 수행합니다.
# 
# 아래 구조에서 user/가 패키지(Package)이며, service.py, repository.py, validator.py들이 모듈(Module)입니다.
# project/
# ├── main.py
# └── user/
#     ├── __init__.py
#     ├── service.py
#     ├── repository.py
#     └── validator.py

# { Package를 사용하는 이유 }
# 관심사 즉, 역할을 분리할 수 있기 때문입니다. 관련된 코드를 하나의 논리적인 공간으로 묶는 것이죠.
#
# { Package와 Module의 관계 }
# Module은 코드가 들어있는 하나의 단위이고, Package는 Module들을 구조적으로 묶는 단위입니다. (헷갈리면 안 되닌 암기 정도는 해둡시다.)
#
# { Package의 Module을 import하기 }
# Package -> Module -> 함수
from intermediate.module_package.calculator import add, subtract

# 불러온 함수 호출
print(add(5, 5)) # 10
print(subtract(5, 5)) # 0
