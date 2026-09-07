# [ 반복문(for, while) ]
# 반목문은 같은 작업을 여러 번 실행하는 문법이며 기본 형식을 다음과 같습니다.
# 
# { 형식 }
#  for 변수 in 반복할 대상:
#      실행할 코드

# { range }
# range(): 끝자리를 포함하지 않으며 0부터 끝자리 바로 전까지의 숫자를 만들어주는 함수입니다.
#
# Python 2: range(5) -> [0, 1, 2, 3, 4]
# Python 3: range(5) -> range(0, 5)
# 
# range() 함수가 왜 Python 왜 이렇게 바뀌었을까요?
# 메모리를 아끼기 위함입니다. 예를 들어, range(1000000)을 호출한다고 생각해보겠습니다.
# Python 2에서는 100만 개의 숫자가 담긴 거대한 리스트가 메모리에 만들어집니다. 하지만 Python 3에서는 시작값, 끝값, 간격만 저장해두고, 필요할 때 숫자를 하나씩 만들어냅니다.
# 이렇게 필요할 때만 값을 계산하는 방식을 '지연 평가(lazy evaluation)'라고 부릅니다. 메모리를 훨씬 효율적으로 사용할 수 있습니다.
#
# { 내부 동작 원리 }
# 변수 i에 range()에서 만들어진 숫자를 삽입하여 for문 아래 코드를 실행합니다.
# start -> i: 0 -> code run -> i: 1 -> code run -> loop
# 변수 i는 내부 변수이기 때문에 반복문이 끝나면 외부에서는 사용 불가능합니다.

for i in range(5):
    print(i, end = " ") # (terminal print: 0 1 2 3 4)
print() # 줄 바꿈을 위한 코드입니다.

# range(시작, 끝)
for i in range(1, 5):
    print(i, end = " ") # (terminal print: 1 2 3 4)
print()

# range(시작, 끝, 증감)
for i in range(0, 10, 2):
    print(i, end = " ") # (terminal print: 0 2 4 6 8)
print()

# { 자료형을 이용하여 반복문 사용하기 }
# start -> char: P -> code run -> char: y -> code run -> loop
for char in "Python": 
    print(char, end = " ") # (terminal print: P y t h o n)
print()

# list
servers = ["web", "db", "cache"]

for server in servers:
    if server == "web": print("웹 서버 발견") # (terminal print: 웹 서버 발견)
    else: print(server, end = " ") # (terminal print: db cache)
print()

# tuple
tuple_data = ((1, 2), (3, 4), (5, 6)) # 이중 튜플

for (first, last) in tuple_data:
    print(first + last, end = " ") # (terminal print: 3 7 11)
print()

# { for-else }
# for문이 끝까지 수행되면 else 절이 실행되고, break로 빠져나가면 else 절은 실행되지 않습니다.
for i in range(5): # 0 ~ 4
    print(i, end = " ") # (terminal print: 0 1 2 3 4)
else: # 반복문이 종료될 경우
    print("끝") # (terminal print: 끝)

# break로 빠져나와 else 문이 실행되는지 확인하는 코드입니다.
for i in range(5): # 0 ~ 4
    if i == 2: # 순회하면서 i가 2인 경우
        break # 반복문 강제 종료
    print(i, end = " ") # (terminal print: 0 1)
else: # 반복문이 종료될 시 실행되지만 break로 빠져나왔기 때문에 실행되지 않습니다.
    print("끝")
print()

# -----------------------------------------------------------------------------------------------
# [ continue ]
# continue는 현재 반복을 건너뛰는 기능을 합니다. 반복문 자체가 종료되는 것은 아니며, 순회할 대상이 남아 있다면 다음 순번으로 넘어가 반복을 계속합니다.
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks: 
    number = number + 1 
    if mark < 60: # 25, 45는 넘어갑니다.
        continue # 건너뛰기
    print(f"{number}번 학생 축하합니다. 합격입니다.")
    # terminal print: 
    #   1번 학생 축하합니다. 합격입니다.
    #   3번 학생 축하합니다. 합격입니다.
    #   5번 학생 축하합니다. 합격입니다.

# -----------------------------------------------------------------------------------------------
# [ break ]
# break는 해당 스코프를 즉시 종료하는 문법이며, 강제로 빠져나가고 싶을 때 사용합니다.
for i in range(3): # 0 ~ 2
    if i == 1: # 순회하면서 i가 1인 경우
        break # 반복문 강제 종료
    print(i) # (terminal print: 0)

# -----------------------------------------------------------------------------------------------
# [ for - 함수(Functions) ]
# { enumerate() }
# enumerate는 0부터 시작하는 인덱스 번호를 자동으로 생성해주며, 시작 번호를 변경하고 싶다면 다음과 같이 변경할 수 있습니다.
# 
# { 형식 } 
# enumerate(list, index)
# ex. enumerate(names, 1)
names: list[str] = ["Kim", "Lee", "Park"]

for index, name in enumerate(names, 1):
    print(f"{index}: {name}", end = " ") # (terminal print: 1: Kim 2: Lee 3: Park)
print()

# { for - zip() }
# 두 개 이상의 리스트를 동시에 순회하고 싶을 때는 zip 함수를 사용합니다.
korean: list[int] = [85, 90, 70]
english: list[int] = [75, 80, 65]

for name, kor, eng in zip(names, korean, english):
    print(f"{name}: 국어 {kor}점, 영어 {eng}점")
    # terminal print: 
    #   Kim: 국어 85점, 영어 75점
    #   Lee: 국어 90점, 영어 80점
    #   Park: 국어 70점, 영어 65점

# -----------------------------------------------------------------------------------------------
# [ while ]
# while은 조건이 참인 동안 계속 반복하는 문법입니다.
# 아래 변수가 없을 경우 무한 반복되기 때문에 조심해서 사용해야 합니다.
count = 0

while count <= 5: # count가 5보다 작거나 같을 경우
    print(f"count: {count}")
    # terminal print:
    #   count: 0
    #   count: 1
    #   count: 2
    #   count: 3
    #   count: 4
    #   count: 5
    count += 1

# { 무한 반복 } 
# 조건을 True로 설정할 경우 무한 반복되니 컴퓨터를 살리기 위해서라도 조심하는게 좋습니다.
# while True:
#     print("무한 반복")

# -----------------------------------------------------------------------------------------------
# [ 리스트 컴프리헨션(List Comprehension) ]
# Python의 중요 문법 중 하나이기 때문에 익혀두시면 좋을 듯합니다.

# { 정석 방식 }
a: list[int] = [1, 2, 3, 4, 5]
result: list[int] = [] # 반복문을 순환하여 값을 삽입할 빈 배열

for num in a:
    result.append(num * 2) # a의 각 값마다 2씩 곱하여 result 배열에 삽입합니다.
print(f"result: {result}") # (terminal print: result: [2, 4, 6, 8, 10])

# { 리스트 컴프리헨션(List Comprehension) 방식 } 
# 리스트 컴프리헨션 방식은 반복문을 사용하여 새로운 리스트 요소를 삽입할 때 사용하는 문법으로 많이 사용합니다.
# 
# { 형식 } 
# [(표현식) for (항목) in (반복 가능한 객체)]

x: list[int] = [1, 2, 3, 4, 5]
result: list[int] = [num * 2 for num in a]

print(f"list comprehension: {result}") # (terminal print: list comprehension: [2, 4, 6, 8, 10])

# 만약 1, 2, 3, 4, 5 중에서 홀수에만 2을 곱하여 담고 싶다면 리스트 컴프리헨션 안에 if 조건문을 사용하면 됩니다.
# [(표현식) for (항목) in (반복 가능한 객체) if (조건문)]
result = [num * 2 for num in a if (num % 2) != 0]
print(f"(+if) list comprehension: {result}") # (terminal print: (+if) list comprehension: [2, 6, 10])

# -----------------------------------------------------------------------------------------------
# 문제) 반복문을 활용하여 구구단을 만드세요.

# for와 range 함수를 이용한 정석 방식
for i in range(2, 10): # 2 ~ 9
    for j in range(1, 10): # 1 ~ 9
        print(f"{i} x {j} = {i * j}") # 2단부터 9단까지 차례대로 나옵니다.

# 리스트 컴프리헨션 방식
times_tables = [i * j for i in range(2, 10) for j in range(1, 10)] # 2 ~ 9단까지
print(times_tables)
# terminal print:
#   [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 
#   3, 6, 9, 12, 15, 18, 21, 24, 27, 
#   4, 8, 12, 16, 20, 24, 28, 32, 36, 
#   5, 10, 15, 20, 25, 30, 35, 40, 45, 
#   6, 12, 18, 24, 30, 36, 42, 48, 54, 
#   7, 14, 21, 28, 35, 42, 49, 56, 63, 
#   8, 16, 24, 32, 40, 48, 56, 64, 72, 
#   9, 18, 27, 36, 45, 54, 63, 72, 81 ]
