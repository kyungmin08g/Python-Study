# [ 모듈(Module) ]
# Python에서 모듈은 하나의 ~.py 파일이 하나의 모듈을 의미합니다.
#
# 1. 왜 Module이 필요한가?
# 모든 코드를 하나의 파일에 작성하면 금방 문제가 생깁니다. 프로젝트가 커지면 파일 하나가 수천 줄, 수만 줄이 될 수 있기 때문에 역할별로 코드를 나누는 작업이 필요합니다.
# 즉, 관심사를 분리하는 겁니다.
# 
# { 모듈의 정확한 정의 }
# 모듈(Module)은 하나의 .py이 맞기야 하지만 더 정확하게는 Python이 import할 수 있는 하나의 독립적인 namespace이라고 할 수 있습니다. (중요 !!)
# 즉, 모듈은 자신만의 namespace를 가지는 거죠.
# 
# 2. Namespace가 왜 필요한가? 
# 예를 들어서 calculator.py 파일과, string_utils.py 파일에 add()라는 똑같은 함수가 있습니다. 저희는 각각의 add() 함수를 실행시키고 싶습니다. 그럴 때 Namespace의 활용성이 드러납니다. 
#  import calculator
#  import string_utils
#  print(calculator.add(10, 20))
#  print(string_utils.add("hello", "world"))
# 위와 같이 import문을 사용하여 모듈을 불러온 다음 각 모듈에 맞는 add() 함수를 호출하는 겁니다. 이렇게 되면 각각의 add() 함수를 실행시킬 수 있죠.
# 가능한 이유는 각각의 다른 namespace에 있기 때문입니다.

# 해당 코드에서는 calculator.py라는 파일이 Module입니다.
# 아래 코드에서 import문은 Python에게 calculator라는 모듈을 찾아서 사용할 수 있도록 해달라고 요청하는 것입니다.
from calculator import add, subtract # __init__.py 파일에서 이미 정의 해두었기 때문에 user/ 폴더에 접근 없이 가능합니다.

# 각 모듈 함수에 접근
print(add(5, 6)) # 11
print(subtract(6, 2)) # 4

# 아래 코드는 calculator.py 모듈을 가져오고 add() 함수를 따로 가져오겠다는 의미입니다.
from intermediate.module_package.calculator import add, subtract

print(add(10, 20)) # 30
print(subtract(20, 10)) # 10

# 별명 붙이기 - as
import intermediate.module_package.calculator as calc # calculator 모듈을 앞으로 calc라고 부르겠다는 의미입니다.

print(calc.add(20, 30)) # 50
print(calc.subtract(30, 20)) # 10

