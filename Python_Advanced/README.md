# Python BackEnd

## Web Development By Django & Flask

### 1. Python 심화

- 가상환경 설정
  ```bash
  $ python3 -m venv myvenv # 원하는 가상환경 이름
  $ source ./myvenv/bin/activate # 가상환경 활성화
  ```
- 가상환경 폴더 안에서 작업 진행

#### 1. 할당과 복사

- 파이썬에서는 데이터도 객체다.
  - 변수에 데이터가 저장된다. (x)
  - 변수가 데이터를 가리킨다. (o)
    - ex) 리스트의 얕은, 깊은 복사 (`.copy()`)

#### 2. 매개변수

- 위치 가변 매개변수 (`*args`, Positional Variable Length Parameter)
- 키워드 가변 매개변수 (`**kwargs`, Keyword Variable Length Parameter)
  - 개수가 정해지지 않은 매개변수
  - \*args는 튜플형, \*\*kwargs는 딕셔너리형

```python
def print_fruits(*args):
    for arg in args:
        print(arg)

def print_dict(**kwargs):
    for key, value in kwargs.item():
        print(f"{key}:{value}")
```
