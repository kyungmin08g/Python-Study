# [ 콜백 함수(Callback Function) ] - Call + Back (다시 호출하다)

# 콜백 함수는 다른 함수에 인자로 전달되어, 특정 시점에 호출되는 함수입니다.
# 헷갈릴 수 있지만 고차 함수는 함수의 인자를 받거나 반환했을 떄를 의미하고, 콜백 함수는 대상 함수를 의미합니다.
# 직접 함수를 호출하는 게 아니라 다른 함수에게 함수를 넘겨주고 필요할 때 이 함수를 호출하는 것입니다.

def hello_python():
    print("(hello_python) Hello, Python!") # Hello

def execute(callback):
    print("작업 시작")
    callback() # 대상 함수 대신 실행
    print("작업 종료")

# 콜백 함수
# 왜 hello_python 함수가 콜백 함수냐면 hello_python 함수를 execute 함수에 전달했고, execute()가 필요할 때 hello()를 호출했기 때문에 콜백 함수라고 부를 수 있습니다.
execute(hello_python)