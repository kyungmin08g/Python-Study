# [ 열거형(Enum) ] (= Java의 enum class과 동일)
# Enum은 Enumeration의 줄임말이며, 정해진 값들에 이름을 붙여 표현하는 기능입니다.

# { Enum을 왜 사용하는가? }
# status = "running" 이렇게 사용하는 것보다 ENUM을 하나 만들어 관리하는 것이 더 좋기 때문입니다. (의미 명확)
# 서버 상태, 사용자 권한, HTTP 상태, 결제 상태, 작업 상태, 로그 레벨, 환경 종류, 지역, 리소스 타입를 표현할 때 좋습니다.

from dataclasses import dataclass
from enum import Enum, IntEnum, StrEnum

@dataclass
class Server:
    name: str
    ip: str
    # 이렇게 dataclass의 필드 타입으로 들어갈 수 있습니다.
    # 이렇게 되면 status 필드는 ServerStatus 타입의 값을 기대한다는 의미가 되겠죠.
    status: ServerStatus

# 서버 상태 Enum
class ServerStatus(Enum):
    RUNNING = "running" # 서버 실행 중 상태
    STOPPED = "stopped" # 서버 중단된 상태
    ERROR = "error" # 서버 에러 상태

status = ServerStatus.RUNNING # ServerStatus.RUNNING 자체가 하나의 Enum 멤버입니다.

# 특정 Enum 값에 접근
print(ServerStatus.RUNNING.value) # running

# 특정 Enum 이름에 접근
print(ServerStatus.RUNNING.name) # RUNNING

# 반대로 값으로 Enum 멤버를 찾을 수도 있습니다.
status = ServerStatus("running")
print(status) # ServerStatus.RUNNING

# [ Enum의 종류 ] - IntEnum, StrEnum
# IntEnum -> 정수 값을 가지면서 정수와의 호환성이 필요한 Enum
# StrEnum -> 문자열과의 호환성이 필요한 Enum
# 
# { IntEnum }
# IntEnum은 대표적으로 HTTP 상태 코드, 파일 권한, 프로토콜의 숫자 코드, OS/API에서 사용하는 정수 상수, 우선순위, 비트 플래그와 연관된 일부 값에 사용됩니다.
# 즉, 원래부터 숫자 자체가 의미를 갖는 경우 적합합니다.
class HttpStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

status = HttpStatus.OK
print(status.value) # 200

# IntEnum 멤버는 int의 성질도 가지고 있기 때문에 int 연관 연산이 가능합니다. (IntEnum -> Enum + int 호환성)
print(status == 200) # True
print(status + 1) # 201 (int 연산 당연히 되죠.)

# { StrEnum }
# Python 3.11부터 표준 라이브러리에 제공되며, Enum 멤버가 있으면서 문자열처럼 사용할 수 있습니다.
# StrEnum -> Enum 멤버가 문자열과 호환됩니다.
# StrEnum을 대표적으로 JSON, 환경 변수, HTTP 헤더, API 요청/응답, 설정 파일, 로그, CLI 옵션에서 많이 사용합니다.
# 즉, 대부분 문자열을 사용할 떄 많이 쓰이죠.

# 명확한 의미를 가지면서 문자열 기반 API와도 잘 연결할 수 있습니다.
class Environment(StrEnum):
    DEV = "dev"
    PROD = "prod"

print(Environment.PROD == "prod") # True (str type과 관련되 연산이기 때문에 당연히 됩니다.)

# { Flag }
# Flag는 Enum과 목적이 다르며, 여러 옵션을 동시에 선택하는 비트 플래그를 표현할 때 쓰입니다.
from enum import Flag, auto, IntFlag

# Enum은 한 개만 선택 가능했지만 Flag는 여러 개를 조합할 수 있습니다.
class PermissionFlag(Flag):
    # auto(): Enum에는 값을 직접 지정하지 않고 자동으로 생성하는 방법 (값 자동 할당)
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

permission = PermissionFlag.READ | PermissionFlag.WRITE
print(permission) # Permission.READ|WRITE (이런 식으로 조합할 수 있습니다.)

# { IntFlag }
# IntFlag는 Flag의 기능에 int 호환성을 더한 것입니다.
# 아래와 같은 비트 연산(|, &, ~, <<)을 할 수 있습니다.
class PermissionIntFlag(IntFlag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

permission = PermissionIntFlag.READ | PermissionIntFlag.WRITE
print(permission) # 3
