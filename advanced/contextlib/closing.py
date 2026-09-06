# [ closing ]
# closing()은 close() 메서드를 가진 객체를 with 문으로 안전하게 관리하기 위한 Context Manager입니다.
# (closing = close()를 with 문에 연결해주는 도구)

from contextlib import closing
# with closing(객체) as obj: ...
# 해당 블록이 끝나면 자동으로 obj.close() 닫아줍니다.

# { 왜 필요할까요? }
# 예를 들어 어떤 객체가 다음처럼 close()를 제공한다고 해봅시다.
class Connection:
    def connect(self):
        print("연결")

    def close(self):
        print("연결 종료")

conn = Connection() # 객체 생성
try: conn.connect()
finally: conn.close() # finally문으로 꼭 반드시 연결을 끊어주기

# { closing 사용 }
from contextlib import closing

with closing(Connection()) as conn:
    conn.connect()
# 끝나면 자동으로 conn.close() 호출해주어 연결을 끊습니다.
# 즉, [ with 시작 -> 객체 사용 -> with 종료 -> close() 자동 호출 ] 흐름으로 동작합니다.

# { open()과 비교 }
# with open("test.txt") as f: ...
# 위 코드에서는 closing()이 필요 없습니다.
# open()이 반환하는 파일 객체 자체가 이미 Context Manager Protocol을 구현하고 있기 때문이죠.
