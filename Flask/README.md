# Python BackEnd

## Web Development By Django & Flask

### Flask 개념

- flask 1.1.2 version으로 강의를 진행
- 21년 5월 22일 2.0.1 버전 릴리즈

- 참고 링크
  ["Google Keep: 구글 킵 클론코딩, Fastcampus 2021"](https://hidekuma.github.io/tutorials/python/flask/gogglekaap)

- 미리 알고 있으면 좋은 지식들

  - [x] Python
    - virtualenv
    - Python script 실행방법
  - [x] pip
  - [ ] Docker
    - [얄코 도커](https://www.yalco.kr/36_docker/)
    - [이성미 도커](https://www.youtube.com/watch?v=3HId-tpYaZs&ab_channel=TTABAE-LEARN)
  - [x] git
  - [x] HTML, CSS, JS

- 기초에서 만든 기능을 토대로 Google Keep 클론코딩을 진행합니다.
  - 메모 추가, 수정, 삭제, 편집, 복구
  - 메모 이미지 삽입 기능
  - 메모 라벨링 기능
  - 메모 페이지네이션
  - 메모 검색
  - 각 기능 API 작성
  - API 문서 자동화
  - 데이터베이스 마이그레이션
- 기초와는 다르게 동적인 페이지를 작성합니다.

#### MSA란?

- Microservices Architecture

#### flask 설치

- conda를 이용하여 가상환경 flask_lecture에서 진행

```zsh
$ pip install flask==1.1.2
$ pip freeze > requirements.txt
```

# gogglekaap

Google keep Clone coding

- flask 실행해보기
  [app.py 작성](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

```zsh
# gogglekaap/app.py 해당 경로에 있는 app을 실행해라
$ export FLASK_APP=gogglekaap/app.py:app
$ flask run

# Debug Mode로 전환, 변경사항 리프레쉬로 반영
$ export FLASK_ENV=development
```

```zsh
$ export FLASK_APP=gogglekaap/app.py:app
$ flask run
```

실행 시, `__name__`이 `app`으로 설정 됨. (앞으로는 이 방법을 사용)

```zsh
$ python gogglekaap/app.py
```

실행 시, `__name__`이 `__main__`으로 설정 됨.

[create_app 작성 및 이해](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/)

gogglekaap폴더에 init.py 파일을 만들어서 모듈화

```python
# __init__.py
from flask import Flask


def create_app():
    print('run: create_app()')
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!!'

    return app
```

이제 환경변수 변경

```
export FLASK_APP=gogglekaap
```

이렇게 실행. FLASK가 `__init__.py`을 먼저 실행하여 `create_app()`을 실행시킴
