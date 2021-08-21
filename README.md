# Python BackEnd

## Web Development By Django & Flask

<hr>

### Python 개념

#### 1. class

1. class?
    - 클래스는 객체를 만들기 위한 설계도
    - 객체는 설계도로부터 만들어낸 제품

</br>

2. class의 속성(attribute)과 메서드(method)
    ```python
    class Monster:
    def __init__(self, health, attack, speed):
        # 얘네가 속성
        self.health = health
        self.attack = attack
        self.speed = speed

    # 얘네가 메서드
    def decrease_health(self, num):
        self.health -= num
    
    def get_health(self):
        return self.health

    # 인스턴스 생성
    goblin = Monster(800, 120, 300)
    wolf = Monster(1500, 200, 350)
    
    # 인트턴스의 속성 호출
    print(goblin.health)
    
    # 인스턴스의 메서드 호출
    goblin.decrease_health(100)
    goblin.get_health()
    ```

    - __init__은 instance를 만들때 반드시 호출되는 메서드
    - self는 instance 자기 자신을 뜻함
    - instance를 생성할 때, 해당 instance가 self자리에 들어간다고 생각하면 됨
    - 생성자: 인스턴스를 만들 때 호출되는 메서드

</br>

3. 파이썬에서는 자료형도 클래스다!
    ```python
    a = 10
    b = '문자열 객체'
    c = True

    print(type(a))
    print(type(b))
    print(type(c))

    >>> <class 'int'>
    >>> <class 'str'>
    >>> <class 'bool'>
    ```

</br>

4. 상속
    - 클래스들의 중복을 제거하고 유지보수를 편하게 하기위해 사용.
    - 자식클래스가 부모클래스의 속성과 메서드를 가져올 수 있음
    - 메서드 오버라이딩: 부모 클래스의 메서드를 자식 클래스에서 재정의


#### 2. module

1. module?
    - 한 개의 완성된 프로그램 파일
    - 내장모듈: 파이썬 설치 시 자동으로 설치되는 모듈
    - 외부모듈: 다른 사람이 만든 파이썬 파일을 pip로 설치해서 사용

</br>

2. module을 사용하는 법

    ```python
    import math
    print(math.pi)
    print(math.ceil(2.5))

    or

    from math import pi, ceil
    print(pi)
    print(ceil(2.5))

    or

    from math import pi, ceil as c
    print(pi)
    print(c(2.5))
    ```

</br>

3. `if __name__ == "__main__":` 이란?
    - 해당 파일을 직접 실행했을 떄만 실행된다.
    - 예를 들어,
    ```python
    # 외부에서 모듈을 실행하면 __name__이 "__main__"이 아닌 해당 모듈의 이름을 반환함
    # module.ipynb
    print(pay_module.__name__)

    >>> pay_module

    # pay_module.py
    print(__name__)

    >>> __main__
    ```

</br>

4. package
    - 관련 있는 모둘을 하나의 폴더로 구성해 놓은 것.
    ```
    startcoding/
        unit/
            __init__.py
            character.py
            item.py
            monster.py
        main.py
    ```

    ```python
    # 1. import 패키지.모듈

    import unit.character
    unit.character.test()

    # 2. from 패키지 import 모듈

    from unit import item
    item.test()

    # 3. from 패키지 import *

    from unit import *
    character.test()
    item.test()
    monster.test()

    # 4. import 패키지

    import unit
    unit.character.test()
    unit.item.test()
    unit.monster.test()
    ```
