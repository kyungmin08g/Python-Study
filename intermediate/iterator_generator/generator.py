# [ 제너레티어(Generator) ]
# 제너레이터는 yield 키워드를 사용하여 값을 필요할 때마다 하나씩 생성하는 Iterator입니다.
# 제너레이터는 이전에 어디에서 멈췄는지 기억하고 있기 때문에 next() 함수를 실행하고 다시 next() 함수를 실행하면 다음 순번이 나옵니다.
# 
# 특히 클라우드 / 서버 / 대규모 트래픽 / 데이터 처리 쪽에서도 유용합니다.
# 예를 들어 엄청나게 큰 로그 파일을 전부 메모리에 올리는 것보다, Iterator로 한 줄씩 처리하는 것이 훨씬 효율적인 경우가 많기 때문입니다.

def count(max_value):
    current = 1 # 현재 값

    # 현재 값(current)이 마지막 순번(max_value)과 비교하여 작거나 같을 경우 아래 코드를 실행합니다.
    while current <= max_value:
        # { return과 yield의 차이 }
        # return은 완전 종료이고, yield는 함수의 상태를 유지한 채 일시 정지를 하는 키워드입니다.
        # 제일 중요한 관계 중 하나는 Generator는 Iterator입니다. Iterator의 복잡한 구현을 Generator가 해주는 것입니다.
        yield current # 제너레이터 함수가 반환하는 제너레이터 객체는 Iterator입니다.
        current += 1 # 현재 값을 늘려줌

try:
    # Generator 생성
    generator = count(3)

    # 예외 없이 순탄하게 반족 처리됩니다.
    for num in generator:
        print(num) # 1, 2, 3

    print(next(generator)) # 1
    print(next(generator)) # 2
    print(next(generator)) # 3
    print(next(generator)) # StopIteration 예외 발생
except StopIteration:
    print("StopIteration 예외가 발생했습니다.")

# Generator가 왜 중요할까요? 바로 메모리 효율 때문입니다.
def get_numbers():
    # yield를 단순히 '값을 반환한다'라고 이해하면 안 되고 yield는 '값을 전달하고, 함수의 실행 상태를 보존한 채 일시중단하는 역할을 하고 있다'라고 기억해두면 좋을 것 같습니다.
    # yield는 반환 + 실행 일시 정지 + 상태 보존을 합친 개념이라고 볼 수 있겠습니다.

    # yield: 값을 전달하고 실행을 일시 정지
    yield 1 
    yield 2 # yield 1 실행 후 실행합니다. (즉, 일시정지죠. (= 이전 상태를 기억하고 있는 상태입니다.))
    yield 3 # yield 2 실행 후 실행합니다. 
    # yield 3 실행 후 실행하지만 이후 없다면 StopIteration 예외를 발생시킵니다.

numbers = get_numbers()
print(next(numbers)) # 1
print(next(numbers)) # 위 설명을 읽었다면 next() 함수를 실행할 때 다음 순번이 나온다는 것을 이해했을 겁니다. (출력: 2)
print(next(numbers)) # 3
# 즉, get_numbers()를 호출했다고 해서 1, 2, 3이 바로 만들어지는 게 아닙니다.
# 그러니까 1, 2, 3을 바로 메모리에 올려두는 것이 아닌 하나씩 꺼내서 올려두기 때문에 메모리 효율이 좋아집니다. yield는 return이랑 다릅니다!! 알고 계셔야 합니다.

# [ 지연 평가(Lazy Evaluation) ]
def nums():
    for i in range(1, 6):
        print(f"{i} 생성")
        yield i

g = nums()
print(next(g)) # 비로소 next(g) 함수를 호출해야 1이 생성됩니다. 즉, 필요할 때 계산한다는 엄청한 특징이 있습니다. 그래서 대용량 데이터에서 강력한 것입니다.
# 한꺼번에 메모리에 올려두는 것이 아닌 필요할 때만 올리는 겁니다.
