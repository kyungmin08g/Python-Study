# [ deque ]
# deque은 양쪽 끝에서 데이터를 빠르게 넣고 빼기 위한 자료구조입니다. (Double-Ended Queue = 양방향 큐)

# list와 비교해서 왜 deque가 필요한지 이해해보겠습니다.
from collections import deque

# 객체 생성
queue = deque()

# 데이터 삽입
queue.append(10)
queue.append(20)
queue.append(30)

print(queue) # deque([10, 20, 30])
# list로 표현하면 오른쪽과 같이 됩니다. -> numbers = [10, 20, 30]
# 하지만 deque는 왼쪽과 오른쪽 양쪽에서 효율적으로 데이터를 추가/삭제할 수 있습니다. (= 즉, Queue)
# 그래서 deque는 양쪽 끝을 사용할 수 있기 때문에 Double-Ended Queue라고 부르는 것입니다.

# 오른쪽에 추가 - append()
queue.append(40)
print(queue) # deque([10, 20, 30, 40])

# 왼쪽의 추가 - appendleft()
queue.appendleft(5)
print(queue) # deque([5, 10, 20, 30, 40])

# 오른쪽에서 제거 — pop()
value = queue.pop()
print(value) # 40
print(queue) # deque([5, 10, 20, 30])

# 왼쪽에서 제거 — popleft()
value = queue.popleft()
print(value) # 5
print(queue) # deque([10, 20])

# [ 그런데 list로 하면 안 되나? ]
# 오른쪽 끝에서 넣고 빼는 것은 list도 잘합니다.
numbers = [10, 20, 30]

numbers.append(40)
print(numbers) # [10, 20, 30, 40]

numbers.pop()
print(numbers) # [10, 20, 30]
# 단, 왼쪽의 있는 데이터를 빼낼 때, 추가할 때가 문제가 됩니다.
# 왜냐하면 뒤에 있는 요소들을 전부 이동시켜야 하기 때문에 list에서 비효율적입니다.
# 
# 왜 list의 pop(0)이 왜 느린가?
# [10, 20, 30, 40]
numbers.pop(0)
# 20: 0번 위치, 30: 1번 위치, 40: 2번 위치 
# 이런 식으로 뒤쪽 요소들을 앞으로 이동시켜야 합니다. 데이터가 5개면 별문제가 되진 않지만 데이터가 10,000개, 1,000,000개, 10,000,000개가 됐을 때는 효율이 급격하게 떨어집니다.
# 
# deque의 popleft()는 양쪽 끝에서 추가/삭제하도록 설계된 자료구조라서 왼쪽에서 제거하는 작업을 효율적으로 처리할 수 있습니다. 그래서 큐 구현에서 굉장히 자주 사용됩니다.

# { maxlen }
# 크기가 제한된 deque입니다. 즉, 큐의 크기를 제한하여 데이터를 삽입하고 뺀다는 것이죠.
logs = deque(maxlen=3)

logs.append("log1")
logs.append("log2")
logs.append("log3")

print(logs) # deque(['log1', 'log2', 'log3'], maxlen=3)

# 하나 더 추가할 시
logs.append("log4")
# 가장 오래된 "log1"이 자동으로 제거됐습니다.
print(logs) # deque(['log2', 'log3', 'log4'], maxlen=3)

# { rotate() }
queue = deque([1, 2, 3, 4, 5])
queue.rotate(1)

# 오른쪽으로 한 칸 회전합니다.
print(queue) # deque([5, 1, 2, 3, 4])
# 1 2 3 4 5 -> rotate(1) -> 5 1 2 3 4

# 또 반대로도 할 수 있습니다.
# deque([5, 1, 2, 3, 4]) 이 상태에서 왼쪽으로 한 칸 이동합니다.
queue.rotate(-1)
print(queue) # deque([1, 2, 3, 4, 5])

# [ 예제 — 최근 요청 5개 ]
recent_requests = deque(maxlen = 5) # 최대 5개의 데이터만 넣을 수 있기 때문에 큐의 크기는 5입니다.

recent_requests.append("/login")
recent_requests.append("/users")
recent_requests.append("/admin")
recent_requests.append("/login")
recent_requests.append("/logout")

print(recent_requests) # deque(['/login', '/users', '/admin', '/login', '/logout'], maxlen=5)

# 새로운 요청
recent_requests.append("/password") # 추가
print(recent_requests) # deque(['/users', '/admin', '/login', '/logout', '/password'], maxlen=5)
