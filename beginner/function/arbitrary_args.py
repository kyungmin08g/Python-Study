# [ 가변 매개변수(*args)와 가변 키워드 매개변수(**kwargs) ] (Python의 함수 중 중요한 문법)

# [ *args ]
# 여러 개의 위치 인자(*args)의 전달된 값들은 함수 내부에서 하나의 튜플(tuple)로 묶여 처리됩니다.
# 예를 들면 특정 함수 인수에 1, 2, 3을 넣는다고 했을 때 (1, 2, 3) 형태로 담겨져 전달 받습니다. 사용할 때는 tuple 형태에서 데이터를 꺼내어 사용됩니다.
# 
# { 형식 }
# def function_name(*parameter) -> type hint:
#       code to run

# [ **kwargs ]
# 키워드 매개변수(**kwargs)는 함수 호출 시 keyword=value 형태로 전달하는 매개변수를 받을 때 사용합니다. 
# 사용할 때는 매개변수 앞에 별 2개(**)를 붙입니다.
# 
# { 형식 }
# def function_name(**parameter) -> type hint:
#       code to run

# [ 가변 매개변수(*args) ]
# 여러 개의 매개변수를 받아 tuple 형태가 맞는지 확인하는 함수입니다.
def print_fruits(categorize, *args) -> None:
    print(f"{categorize}: {args}")
    
    for fruit in args:
        print(fruit, end = " ") # (terminal print: apple banana grape)

# 함수의 매개변수에는 (apple, banana, grape) tuple 형태로 담겨져 있습니다.
print_fruits("fruit", "apple", "banana", "grape") # 함수 호출과 동시에 내부 코드 실행
print() # 줄 바꿈 용도입니다.

# [ 가변 키워드 매개변수(**kwargs) ]
# 사용자 프로필 정보 출력 함수
def create_profile(**info):
    print("=== 프로필 정보 ===") # (terminal print: === 프로필 정보 ===)
    for key, value in info.items(): # key=value 형태이기 때문에 다음과 같이 작성해줍니다.
        print(f"{key}: {value}")
        # terminal print: 
        #   name: Kyungmin Kim
        #   age: 20
        #   job: programmer
        #   hobby: reading
    
    print(f"(Dict 형태: {info})") # (terminal print: (Dict 형태: {'name': 'Kyungmin Kim', 'age': 20, 'job': 'programmer', 'hobby': 'reading'})) key=value 형태이니 dict type입니다.

# 결국 {'name': 'Kyungmin Kim', 'age': 20, 'job': 'programmer', 'hobby': 'reading'} 형태가 완성되며, 함수의 인수에 dict 형태로 담겨집니다.
create_profile(name="Kyungmin Kim", age=20, job='programmer', hobby='reading') # 함수 호출과 동시에 내부 동작 수행

# 둘 다 하나씩 사용하는게 아닌 같이 사용해도 충분히 됩니다. ex. def f1(param, *args, **kwargs):
