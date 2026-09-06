# [ 이터레이터(iterator) ]
# next() 함수로 값을 하나씩 꺼낼 수 있는 객체입니다.

# { 예제 01 }
numbers: list[int] = [10, 20, 30]

# 우리는 for문이 알아서 하나씩 꺼내준다고 생각하지만, 내부적으로는 이터레이터(iterator)를 사용해서 하나씩 꺼내고 있다는 사실, 알고 계셨나요?
for num in numbers:
    print(num)
# [10, 20, 30] -> iter() -> Iterator -> next() -> 10 next() -> 20 next() -> 30 next() -> StopIteration 구조로 동작합니다.
# 지금은 이게 무슨 소리인지 이해 못 할 것 같아 다음으로 넘어가도록 하겠습니다.

# [ Iterable과 Iterator ]
# 이 둘을 구분할 수 있어야 합니다.
# Iterable은 반복할 수 있는 객체를 의미합니다. 대표적으로 list, tuple, str, dict, set, range 등이 있습니다.
# 즉, numbers = [10, 20, 30]는 Iterable입니다. (반복 가능한 객체니까 말이죠.)
# 
# Iterator는 실제로 데이터를 하나씩 꺼내주는 객체입니다. next() 함수를 통해 자료형이 있는 값들을 하나씩 꺼내주는 역할을 합니다.
# numbers -> iter() -> iterator
# 
# iter() 함수는 Iterable로부터 Iterator를 만드는 역할합니다.
# iter(numbers)의 의미는 사실 "numbers에서 데이터를 하나씩 꺼낼 수 있는 Iterator를 만들어달라"는 것과 동일합니다.
# 
# next() 함수는 Iterator에게 다음 데이터 하나 달라고 요청하는 역할을 합니다.
# Iterator 내부적으로는 현재 위치를 기억하며, next() 함수로 마지막 데이터를 꺼낸 후 다음 데이터를 꺼낼려고 할 때 StopIteration 예외가 발생합니다.
# 내부적으로 현재 위치를 기억하는데 다음 데이터가 없을 경우 예외를 발생시키는 거죠. ("경고: 다음 데이터가 없다!!""라면서 말입니다.)

# { 예제 }
numbers = [10, 20, 30]

# iter는 Iterator를 만드는 함수입니다.
iterator = iter(numbers)

# 그렇기 때문에 Iterator를 만들었다면 next() 함수를 사용할 수 있습니다.
print(next(iterator)) # 10
print(next(iterator)) # 20
print(next(iterator)) # 30
# print(next(iterator)) # StopIteration 예외 발생

# { for문의 내부 동작 방식 }
numbers = [10, 20, 30]
iterator = iter(numbers) # iterator 생성

while True:
    try: # 예외 처리를 위해서 try-except 문법을 사용해줍니다.
        number = next(iterator) # next() 함수로 다음 데이터 꺼냄
        print(number) # 10, 20, 30
    except StopIteration: # next() 함수로 데이터를 꺼낼 때 iterator에 더 이상 꺼낼 데이터가 없으면 StopIteration 예외를 발생시킵니다.
        break # 예외를 발생시키면 break로 그냥 종료하겠다라는 의미입니다.
# for문의 내부 동작 방식입니다.

# { 지금까지 배운 이론 정리 }
# Iterable: 반복할 수 있는 객체
# Iterator: 데이터를 하나씩 꺼내는 객체
# iter(): Iterable -> Iterator
# next(): Iterator -> 다음 값 (없을 경우 StopIteration 예외 발생)

# [ 사용자 정의 Iterator 만들어보기 ] - 내부 동작 원리 이해
# Python에서 Iterator가 되려면 기본적으로 다음 두 메서드를 제공해야 합니다.
# __iter__(), __next__()

# { 예제 }
# 실제 내부 동작과 다를 수 있으니 그냥 예제로만 봐주세요 !!
class CustomIterator:
    # 기본 생성자
    def __init__(self, max_value) -> None:
        self.current = 1
        self.max_value = max_value

    # Iterable한 객체를 Iterator 객체로 변경해주는 메소드
    def __iter__(self):
        return self # iter() 함수를 호출하면 자동으로 __iter__ 매직 메소드가 호출되도록 설정하며, 자신의 객체를 반환합니다.

    # Iterator 객체에서 다음 값을 하나씩 꺼내는 역할해주는 메소드
    def __next__(self):
        # 이전 호출에서 정한 다음 순번을 마지막 순번이랑 비교하여 높을 경우 기존 next() 함수와 같이 StopIteration 예외를 발생시킵니다.
        if self.current > self.max_value: # 마지막 순번(데이터)보다 더 높을 경우
            raise StopIteration # 예외 발생

        value = self.current # 반환할 값 저장
        self.current += 1 # 변수에 다음 순번을 저장 (만약 첫 순번을 반환 값으로 정했다면 다음 순번을 저장)

        return value # 값 반환

# 사용
try:
    iterator = CustomIterator(3) # 사용자 정의 Iterator 객체 생성

    print(next(iterator)) # 1
    print(next(iterator)) # 2
    print(next(iterator)) # 3
    print(next(iterator)) # StopIteration 예외 발생
except StopIteration:
    print("StopIteration 예외가 발생했습니다!!")

# 사용자 정의 Iterator로 만들려면 위와 같이 복잡한 코드를 작성해야 합니다.
# Python에는 이것을 훨씬 간단하게 만드는 기능을 제공하는데 이를 제너레이터(Generator)라고 부릅니다.
