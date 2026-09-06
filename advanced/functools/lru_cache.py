# [ lru_cache ]
# LRU(Least Recently Used) + cache 즉, 가장 오랫동안 사용되지 않은 캐시를 의미하며, 캐시 크기를 관리해야 할 때 주로 많이 사용됩니다.
# * lru_cache, cache 모두 함수의 실행 결과를 저장해 두었다가 같은 입력이 다시 들어오면 재계산하지 않고 저장된 결과를 반환하는 캐싱 도구입니다.
# 
# 중요한 점은 캐시되는 함수의 인자는 hashable해야 한다는 점입니다.
# 캐시는 기본적으로 같은 입력이면 같은 결과가 나오는 함수라고 생각하면 편합니다.
# 캐싱은 계산 비용이 크고 + 같은 입력이 반복해서 들어오며 + 결과를 재사용할 수 있을 때 효과적입니다.

# 먼저 캐싱이 무엇일까요?
def square(x):
    print("계산 중...")
    return x * x

print(square(10)) # 계산 중... 100
# 이미 10 -> 100이라는 결과를 알고 있는데도 다시 계산합니다.
print(square(10)) # 계산 중... 100

# 캐싱은 이 결과를 저장해 놓는 것입니다.
# square(10) 계산 -> 10 → 100 저장 -> 다시 square(10) -> "10은 이미 계산했네?" -> 100 반환
# 즉, 실행 결과를 저장해두었다가 같은 입력이 또 다시 들어오면 재계산 하지 않고 저장된 결과를 반환합니다.

from functools import lru_cache

# maxsize: 캐시의 최대 크기
@lru_cache(maxsize = 3)
def lru_cache_square(x):
    print("계산 중...")
    return x * x

print(lru_cache_square(10)) # 계산 중... 100
print(lru_cache_square(10)) # 100
print(lru_cache_square(10)) # 100
# 계산 중...이 한 번만 출력되게 됩니다.
# 즉, 첫 번째 square(10) -> 실제 함수 실행 -> 결과 100 저장 -> 두 번째 square(10) -> 캐시에 10이 있음 -> 100 반환 -> 세 번째 square(10) -> 캐시에 10이 있음 -> 100 반환 흐름으로 흘러갑니다.

print(lru_cache_square(5)) # 계산 중... 25
print(lru_cache_square(5)) # 25
print(lru_cache_square(6)) # 계산 중... 36
print(lru_cache_square(8)) # 계산 중... 64
print(lru_cache_square(8)) # 64

print(lru_cache_square(7)) # 계산 중... 49 (호출하면 캐시 공간이 부족하기 때문에 가장 오래 사용되지 않은 5가 제거됩니다. 이것이 LRU입니다.)
# maxsize는 캐시에 최대 128개의 결과를 저장되며, 128개를 초과하면 LRU 정책에 따라 오래 사용되지 않은 항목부터 제거됩니다.
# 단, maxsize을 None으로 설정하면 캐시 크기에 제한이 없습니다.

# 캐시의 통계를 볼 수 있습니다. cache_info()
# hits: 캐시에서 결과를 찾은 횟수, misses: 캐시에 없어서 실제 함수를 실행한 횟수, maxsize: 최대 캐시 크기, currsize: 현재 캐시에 저장된 항목 수
print(lru_cache_square.cache_info()) # CacheInfo(hits=4, misses=5, maxsize=3, currsize=3)

# 캐시 비우기
lru_cache_square.cache_clear()

# [ cache ]
# cache는 사실상 @lru_cache(maxsize = None)과 같은 목적의 간단한 형태라고 이해하면 됩니다. 즉, @cache -> 캐시 크기 제한 없음
# 제한 없는 캐시가 적절할 때 많이 사용합니다.
from functools import cache

@cache
def cache_square(x):
    return x * x
