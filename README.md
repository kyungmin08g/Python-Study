# 🐍 Python Study

> Python의 기본부터 고급 기능까지 학습하고, 이를 **Backend → AWS → Cloud Security**로 확장합니다.

Python 문법을 단순히 암기하는 것이 아니라 **핵심 개념과 동작 원리를 이해하고 직접 구현하는 것**을 목표로 합니다.

---

## 📊 Progress

| Stage             | Progress |   Status   |
| :---------------- | :------: | :--------: |
| 🟢 Beginner       |  `100%`  | ✅ Complete |
| 🟡 Intermediate   |  `100%`  | ✅ Complete |
| 🔴 Advanced       |  `100%`  | ✅ Complete |
| ⚡ FastAPI         |   `0%`   |   ⏳ Next   |
| 🌐 Backend        |   `0%`   |  ⏳ Planned |
| 🐳 Docker         |   `0%`   |  ⏳ Planned |
| ☁️ AWS            |   `0%`   |  ⏳ Planned |
| 🔐 Cloud Security |   `0%`   |   🎯 Goal  |

**Current:** `Advanced → FastAPI`

---

## 🗺️ Roadmap

```text
🟢 Beginner → 🟡 Intermediate → 🔴 Advanced → ⚡ FastAPI → 🌐 Backend → 🐳 Docker → ☁️ AWS → 🔐 Cloud Security
   100%            100%             100%          Next        Planned       Planned      Planned         Goal
```

---

# 📚 Learning Progress

## 🟢 Beginner · 100%

| Basics       | Control     | Function              |
| ------------ | ----------- | --------------------- |
| ✅ Variables  | ✅ Condition | ✅ Function            |
| ✅ Data Types | ✅ Loop      | ✅ Arbitrary Arguments |
| ✅ Operators  |             | ✅ Lambda              |
| ✅ Slicing    |             |                       |
| ✅ Dictionary |             |                       |

---

## 🟡 Intermediate · 100%

| Function                | OOP             | Iteration   | Structure       |
| ----------------------- | --------------- | ----------- | --------------- |
| ✅ Higher-Order Function | ✅ Class         | ✅ Iterator  | ✅ Module        |
| ✅ Callback              | ✅ Encapsulation | ✅ Generator | ✅ Package       |
| ✅ Closure               | ✅ Inheritance   |             | ✅ `__init__.py` |
| ✅ Decorator             | ✅ Overriding    |             |                 |
|                         | ✅ Polymorphism  |             |                 |
|                         | ✅ Abstraction   |             |                 |
|                         | ✅ Class Method  |             |                 |
|                         | ✅ Static Method |             |                 |
|                         | ✅ Dunder Method |             |                 |

---

## 🔴 Advanced · 100%

| Context            | Collections   | Functools        | Typing        | Exception             |
| ------------------ | ------------- | ---------------- | ------------- | --------------------- |
| ✅ Context Manager  | ✅ Counter     | ✅ partial        | ✅ Type Hint   | ✅ Exception Handling  |
| ✅ `with` Statement | ✅ defaultdict | ✅ wraps          | ✅ Generic     | ✅ Custom Exception    |
| ✅ `contextlib`     | ✅ deque       | ✅ lru_cache      | ✅ TypeVar     | ✅ Exception Hierarchy |
|                    | ✅ namedtuple  | ✅ reduce         | ✅ Protocol    | ✅ Exception Chaining  |
|                    | ✅ ChainMap    | ✅ singledispatch | ✅ Callable    |                       |
|                    |               |                  | ✅ Literal     |                       |
|                    |               |                  | ✅ TypedDict   |                       |
|                    |               |                  | ✅ Annotated   |                       |
|                    |               |                  | ✅ Any / Never |                       |

---

# 📁 Project Structure

```text
python-study/
│
├── README.md
├── .gitignore
│
├── 🟢 beginner/
│   ├── basics/
│   │   ├── variable.py
│   │   ├── type.py
│   │   ├── operator.py
│   │   ├── slicing.py
│   │   └── dict.py
│   ├── control/
│   │   ├── condition.py
│   │   └── loop.py
│   └── function/
│       ├── function.py
│       ├── arbitrary_args.py
│       └── lambda.py
│
├── 🟡 intermediate/
│   ├── function/
│   │   ├── higher_order.py
│   │   ├── callback.py
│   │   ├── closure.py
│   │   └── decorator.py
│   ├── oop/
│   │   ├── class_.py
│   │   ├── encapsulation.py
│   │   ├── inheritance.py
│   │   ├── overriding.py
│   │   ├── polymorphism.py
│   │   ├── abstraction.py
│   │   └── methods/
│   │       ├── classmethod.py
│   │       ├── staticmethod.py
│   │       └── dunder_method.py
│   ├── iterator_generator/
│   │   ├── iterator.py
│   │   └── generator.py
│   └── modules_packages/
│       ├── module.py
│       ├── package.py
│       ├── __init__.py
│       └── calculator.py
│
└── 🔴 advanced/
    ├── context_manager/
    │   ├── context_manager.py
    │   └── with_statement.py
    ├── contextlib/
    │   ├── contextmanager.py
    │   ├── closing.py
    │   ├── suppress.py
    │   └── redirect_stdout.py
    ├── collections/
    │   ├── counter.py
    │   ├── defaultdict.py
    │   ├── deque.py
    │   ├── namedtuple.py
    │   └── chain_map.py
    ├── functools/
    │   ├── partial.py
    │   ├── wraps.py
    │   ├── lru_cache.py
    │   ├── reduce.py
    │   └── singledispatch.py
    ├── typing/
    │   ├── type_hint.py
    │   ├── generic.py
    │   ├── typevar.py
    │   ├── protocol.py
    │   ├── callable.py
    │   ├── literal.py
    │   ├── typed_dict.py
    │   ├── annotated.py
    │   ├── any.py
    │   └── never.py
    └── exceptions/
        └── exception_handling.py
```

---

# 🚀 Next Step

Python 학습을 마무리하고 **실제 서비스 개발과 운영 환경**으로 확장합니다.

| Stage           | Topics                                                                          |
| --------------- | ------------------------------------------------------------------------------- |
| ⚡ **FastAPI**   | FastAPI, Pydantic, REST API                                                     |
| 🌐 **Backend**  | SQLAlchemy, PostgreSQL, Redis, Authentication / Authorization                   |
| 🐳 **Docker**   | Container, Docker Compose                                                       |
| ☁️ **AWS**      | VPC, IAM, EC2, ALB, RDS, S3, SQS, CloudWatch                                    |
| 🔐 **Security** | Hardening, Logging, Monitoring, Vulnerability Testing, Mock Hacking, Automation |

---

# 🎯 Goal

### Backend × Cloud × Security × Automation

Python을 기반으로 서비스를 직접 개발하고 운영한 뒤, AWS 환경에서 **보안 설계 → 보안 강화 → 공격 시뮬레이션 → 탐지 및 자동화**까지 경험하는 것을 목표로 합니다.

```text
Python
  ↓
FastAPI
  ↓
Backend
  ↓
Docker
  ↓
AWS
  ↓
Security
  ↓
Automation
  ↓
Cloud Security Engineer
```

> **Python은 목적이 아니라 도구입니다.**
> 최종 목표는 **AWS 기반 Cloud Security Engineering**입니다.
