# [ __init__.py ]
# Package가 import될 때 실행될 초기화 코드를 작성하거나, Package가 외부에 제공할 API를 구성하는 데 사용할 수 있는 특별한 Module입니다.
print("user package loaded")

# __init__.py에 미리 가져올 파일이나 함수를 정의 해놓으면 다른 파일에서 사용할 떄 조금 더 편하게 사용할 수 있습니다.
# .은 무엇을 의미하냐면 현재 경로를 의미합니다. 즉, 현재 작업 중인 패키지(Package)를 의미합니다.
from .calculator import add, subtract
# 실무에서 유용하게 사용될 것 같습니다. (추측)
