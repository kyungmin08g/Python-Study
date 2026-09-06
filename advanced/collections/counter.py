# [ Counter ]
# 값이 몇 번 등장했는지 자동으로 세어주는 자료구조입니다. (= 각 값의 등장 횟수를 세는 딕셔너리)
# 쉽게 말해 빈도수(frequency)를 계산하는 작업을 편하게 해주는 클래스라고 생각해주면 됩니다.

from collections import Counter

# 중복이 있는 배열
numbers = [1, 2, 2, 3, 3, 3]
counter = Counter(numbers)

print(counter) # Counter({3: 3, 2: 2, 1: 1}) -> 1: 1번, 2: 2번, 3: 3번
# 실제로는 딕셔너리처럼 사용할 수 있습니다.
print(counter[1]) # 1
print(counter[2]) # 2
print(counter[3]) # 3

# 문자열
text = "hello"
counter = Counter(text)

# 문자 하나하나의 등장 횟수를 센 것입니다.
print(counter) # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# { most_common() }
# 가장 많이 등장한 것 상위 N개를 가져올 수도 있는 기능을 제공하는 함수입니다.
# 형태: (값, 등장 횟수)
numbers = [1, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(numbers)

print(counter.most_common()) # [(4, 4), (3, 3), (1, 1), (2, 1)]
print(counter.most_common(2)) # [(4, 4), (3, 3)] -> 가장 많이 등장한 값 2개만 뽑아달라는 의미입니다.

# { 없는 값을 조회하면 어떻게 될까요? }
# dict type에서는 예외를 발생시키지만 Counter에서는 새로 만들어준다는 차이점이 있습니다.
data = {}
# print(data["hello"]) # KeyError

counter = Counter("hello")
print(counter["e"]) # 1 -> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1}) 여기서 3번 즉, e를 출력합니다.

# 직접 개수를 추가할 수도 있어습니다.
counter = Counter()

counter["apple"] += 1
counter["apple"] += 1
counter["banana"] += 1

print(counter) # Counter({'apple': 2, 'banana': 1})

# Counter끼리 계산도 가능합니다.
a = Counter({"apple": 3, "banana": 2})
b = Counter({"apple": 1, "banana": 4})

print(a + b) # Counter({'banana': 6, 'apple': 4})

# { 실전에서는 어떻게 쓰일까요? }
# 예를 들어 로그에서 IP 주소가 등장한다고 해봅시다.
ips = [
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.1",
    "10.0.0.3",
    "10.0.0.1",
    "10.0.0.2"
]
request_count = Counter(ips)

# IP별 요청 횟수를 알고 싶다면 다음과 같이 작성하면 됩니다.
# 1.
print(request_count) # Counter({'10.0.0.1': 3, '10.0.0.2': 2, '10.0.0.3': 1})
# 2.
# 가장 요청을 많이 보낸 IP를 찾을 수 있습니다.
print(request_count.most_common(1)) # [('10.0.0.1', 3)]
# (보안 로그 분석에서도 이런 빈도 기반 분석이 자주 나옵니다.)
