class math:

    # 정적 메서드 (static method)
    # 인스턴스를 만들 필요가 없는 메서드
    @staticmethod
    def add(x, y):
        return x+y

    @staticmethod
    def sub(x, y):
        return x-y


print(math.add(3, 2))
print(math.sub(3, 2))
