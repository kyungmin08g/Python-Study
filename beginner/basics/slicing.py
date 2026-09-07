# [ 슬라이싱(Slicing) ]
# 슬라이싱(Slicing)은 배열(list)이나 문자열(str)에서 특정 구간을 잘라내어 가져오는 기능입니다.
# 
# { 형식 }
# 변수명[start:end:step]
# - start (시작 인덱스): 가져올 구간의 시작 위치입니다 (포함)
# - end (끝 인덱스): 멈출 위치입니다 (포함하지 않음, 바로 앞까지만 가져옴)
# - step (간격): 몇 칸씩 건너뛰며 가져올지 설정하며, 생략하면 기본값은 1입니다.

# { 전체 복사 }
a: list[int] = [1, 2, 3]
b: list[int] = a[:] # a list 전체 복사합니다. (a list의 주소값이 아닌, 값 자체를 복사합니다.)
a[0] = 100 # a list의 첫 번째 요소를 100으로 변경합니다.
print(f"a: {a}") # (terminal print: a: [100, 2, 3])
print(f"b: {b}") # (terminal print: b: [1, 2, 3])

# { 일부 복사 }
c: list[int] = a[1:3] # a list의 1번부터 2번까지의 요소를 복사합니다. (0부터 시작이니 3번은 포함하지 않습니다.)
print(f"c: {c}") # (terminal print: c: [2, 3])

d: list[int] = a[1:] # a list의 1번부터 끝까지의 요소를 복사합니다.
print(f"d: {d}") # (terminal print: d: [2, 3])

e: list[int] = a[:2] # a list의 0번부터 1번까지의 요소를 복사합니다.
print(f"e: {e}") # (terminal print: e: [100, 2])

# { 간격 추출 }
interval_array: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 간격 추출할 배열 초기 선언
f: list[int] = interval_array[1::2] # interval_array의 1번부터 9번까지의 요소를 2칸씩 건너뛰며 복사합니다.
print(f"f: {f}") # (terminal print: f: [2, 4, 6, 8, 10])

g: list[int] = interval_array[::3] # interval_array의 0번부터 9번까지의 요소를 3칸씩 건너뛰며 복사합니다.
print(f"g: {f}") # (terminal print: f: [1, 4, 7, 10])

# { 역순 추출 }
h: list[int] = interval_array[::-1] # interval_array의 9번부터 0번까지의 요소를 역순으로 복사합니다.
print(f"h: {g}") # (terminal print: h: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# { copy 모듈 또는 함수 사용 }
# copy() 함수는 [:]와 동일하게 list의 주소값이 아닌, 값 자체를 복사합니다.
from copy import copy # copy 모듈은 객체를 복사할 때 사용합니다.

exmaple_list: list[int] = [1, 2, 3, 4, 5]
exmaple_list_copy: list[int] = copy(exmaple_list)

print(f"exmaple_list: {exmaple_list}") # (terminal print: exmaple_list: [1, 2, 3, 4, 5])
print(f"exmaple_list_copy: {exmaple_list_copy}") # (terminal print: exmaple_list_copy: [1, 2, 3, 4, 5])
print(exmaple_list is exmaple_list_copy) # (terminal print: False)

# list copy() 기본 함수 사용
print(exmaple_list.copy()) # (terminal print: [1, 2, 3, 4, 5])
# exmaple_list의 값 자체를 복사합니다. (주소값이 아닌, 값 자체를 복사합니다.)
