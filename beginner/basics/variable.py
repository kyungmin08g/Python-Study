from typing import Final # Final은 Python@3.8+ 버전부터 내장 모듈에 기본적으로 포함되어 사용할 수 있습니다. (상수 활용 가능)

# 상수
BLOOD_TYPE: Final[str] = "A" # 혈액형은 변하지 않으므로 상수로 선언합니다.

# 변수
name: str = "Kyungmin Kim" # 이름은 변경될 가능성도 있으니 변수로 선언합니다.
age: int = 20 # 해가 갈수록 나이는 변경되니 변수로 선언합니다.

# 실행은 정상적으로 되지만, Final로 선언된 상수는 재할당이 불가능하므로, 이 줄에서 밑줄이 발생합니다.
# (단, Settings에서 type checking -> Type Checking Mode를 strict mode로 설정해야 합니다.)
# BLOOD_TYPE = "O" # 상수임을 알리기 위해 VSCode에서 밑줄이 발생합니다.

# 최종 결과
print(f"name: {name}, age: {age} , blood type: {BLOOD_TYPE}")

# ------------------------------- 변수를 만드는 여러가지 방법 ----------------------------------
# 여러 개의 변수를 한 줄에 선언
h, i, j = 1, 2, 3 # 여러 개의 변수를 한 줄에 선언할 수 있습니다.
print(f"h: {h}, i: {i}, j: {j}") # h: 1, i: 2, j: 3

# 퓨플(tuple)을 활용한 변수 선언
(k, l, m) = (4, 5, 6)
print(f"k: {k}, l: {l}, m: {m}") # k: 4, l: 5, m: 6

# 리스트(list)를 활용한 변수 선언
[o, p] = [7, 8]
print(f"o: {o}, p: {p}") # o: 7, p: 8
