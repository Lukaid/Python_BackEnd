from abc import *


class Item(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다.")

    # 해당 클래스를 상속받는 모든 자식 클래스는 use라는 추상메서드를 반드시 구현해야 함
    @abstractmethod
    def use(self):
        pass


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.damage}로 공격합니다.")


class HealingItem(Item):
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.recovery_amount}회복")


m16 = Weapon("m16", 110)
bungdae = HealingItem("붕대", 20)

m16.use()
bungdae.use()
