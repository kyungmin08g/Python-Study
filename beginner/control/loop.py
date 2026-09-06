# [ 반복문 ] while, for
# 같은 작업을 여러 번 실행하는 문법입니다.

# 형식:
#  for 변수 in 반복할 대상:
#      실행할 코드

# range(int) 함수: 끝자리를 포함하지 않으며 0부터 끝자리 바로 전까지의 숫자를 만들어줍니다.
#
# | Python 2 |
# range(5) -> [0, 1, 2, 3, 4]
# 
# | Python 3 |
# range(5) -> range(0, 5)
# 
# range() 함수가 왜 Python 왜 이렇게 바뀌었을까요?
# 메모리를 아끼기 위함입니다. 예를 들어, range(1000000)을 호출한다고 생각해보겠습니다.
# 
# Python 2에서는 100만 개의 숫자가 담긴 거대한 리스트가 메모리에 만들어집니다.
# Python 3에서는 시작값, 끝값, 간격만 저장해두고, 필요할 때 숫자를 하나씩 만들어냅니다.
# 이렇게 필요할 때만 값을 계산하는 방식을 '지연 평가(lazy evaluation)'라고 부릅니다. 메모리를 훨씬 효율적으로 사용할 수 있습니다.
#
# { 내부 동작 원리 }
# 변수 i에 range()에서 만들어진 숫자를 삽입하여 for문 아래 코드를 실행합니다.
# start -> i: 0 -> code run -> i: 1 -> code run -> loop
# 변수 i는 내부 변수이기 때문에 반복문이 끝나면 외부에서는 사용 불가능합니다.
for i in range(5):
    print(i) # 0, 1, 2, 3, 4

# range(시작, 끝)
for i in range(1, 5):
    print(i) # 1, 2, 3, 4

# range(시작, 끝, 증감)
for i in range(0, 10, 2):
    print(i) # 0, 2, 4, 6, 8

# [ 자료형 사용 ]
# start -> char: P -> code run -> char: y -> code run -> loop
for char in "Python":
    print(char) # P, y, t, h, o, n

servers = ["web", "db", "cache"]

for server in servers:
    if server == "web":
        print("웹 서버 발견") # 웹 서버 발견
    else:
        print(server) # cache

tuple_data = ((1, 2), (3, 4), (5, 6))

for (first, last) in tuple_data:
    print(first + last) # 3, 7, 11

# [ continue문 ]
# 현재 반복을 건너뜁니다. (반복문 자체가 종료되는 것은 아님!) 순회할 대상이 남아 있다면 다음 순번으로 넘어가 반복을 계속합니다.
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks: 
    number = number + 1 
    if mark < 60: # 25, 45는 넘어감
        continue # 건너뛰기
    print(f"{number}번 학생 축하합니다. 합격입니다.") # 1(= 90), 3(= 67), 5(= 80)

# [ break 문 ]
# break 문은 for 문을 강제로 빠져나가고 싶을 때 사용합니다.
for i in range(3): # 0 ~ 2
    if i == 1: # 순회하면서 i가 1인 경우
        break # 반복문 강제 종료
    print(i) # 0

# [ for-else문 ]
# for문이 끝까지 수행되면 else 절이 실행되고, break로 빠져나가면 else 절은 실행되지 않습니다.
for i in range(5): # 0 ~ 4
    print(i) # 0, 1, 2, 3, 4
else: # 반복문이 종료될 시 실행
    print("끝") # 끝 (출력)

# break로 빠져나와 else문이 실행되는지 확인
for i in range(5): # 0 ~ 4
    if i == 2: # 순회하면서 i가 2인 경우
        break # 반복문 강제 종료
    print(i) # 0, 1
else: # 반복문이 종료될 시 실행되지만 break로 빠져나왔기 때문에 실행되지 않습니다.
    print("끝")

# [ for - enumerate() 함수 사용하기 ]
names: list[str] = ["Kim", "Lee", "Park"]

# enumerate는 0부터 시작하는 인덱스 번호를 자동으로 생성해 주며, 시작 번호를 변경하고 싶다면 다음과 같이 변경할 수 있습니다.
# enumerate(list, index) | ex. enumerate(names, 1)
for index, name in enumerate(names, 1):
    print(f"{index}: {name}") # 1: Kim, 2: Lee, 3: Park

# [ for - zip() 함수 사용하기 ]
korean: list[int] = [85, 90, 70]
english: list[int] = [75, 80, 65]

# 두 개 이상의 리스트를 동시에 순회하고 싶을 때는 zip 함수를 사용합니다.
for name, kor, eng in zip(names, korean, english):
    print(f"{name}: 국어 {kor}점, 영어 {eng}점")

# [ while ] - 조건이 참인 동안 계속 반복
count = 0

# while은 위 변수가 없을 경우 무한 반복되기 때문에 조심해서 사용해야 합니다.
while count <= 5:
    print(f"count: {count}")
    count += 1

# 무한 반복
# while True:
#     print("무한 반복")

# [ 리스트 컴프리헨션(List Comprehension) ] 중요 !!
# 정석 방식
a: list[int] = [1, 2, 3, 4, 5]
result: list[int] = [] # 반복문을 순환하여 값을 삽입할 빈 배열

for num in a:
    result.append(num * 2) # a의 각 값마다 2씩 곱하여 result 배열에 넣어줍니다.
print(f"result: {result}") # [2, 4, 6, 8, 10]

# 리스트 컴프리헨션 방식
# 형식: [(표현식) for (항목) in (반복 가능한 객체)]
x: list[int] = [1, 2, 3, 4, 5]
result: list[int] = [num * 2 for num in a]
print(f"list comprehension: {result}") # [2, 4, 6, 8, 10]

# 만약 [1, 2, 3, 4, 5] 중에서 홀수에만 2을 곱하여 담고 싶다면 리스트 컴프리헨션 안에 if 조건문을 사용하면 됩니다.
# 형식: [(표현식) for (항목) in (반복 가능한 객체) if (조건문)]
result = [num * 2 for num in a if (num % 2) != 0]
print(f"(+if) list comprehension: {result}") # [2, 6, 10]

# -----------------------------------------------------------------
# 문제. 반복문을 활용하여 구구단을 만드세요. (간단)

# 정석 방식
for i in range(2, 10): # 2 ~ 9
    for j in range(1, 10): # 1 ~ 9
        print(f"{i} x {j} = {i * j}")

# 리스트 컴프리헨션 방식
times_tables = [i * j for i in range(2, 10)]
print(times_tables)
# [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 
# 3, 6, 9, 12, 15, 18, 21, 24, 27, 
# 4, 8, 12, 16, 20, 24, 28, 32, 36, 
# 5, 10, 15, 20, 25, 30, 35, 40, 45, 
# 6, 12, 18, 24, 30, 36, 42, 48, 54, 
# 7, 14, 21, 28, 35, 42, 49, 56, 63, 
# 8, 16, 24, 32, 40, 48, 56, 64, 72, 
# 9, 18, 27, 36, 45, 54, 63, 72, 81 ]
