class Calculator:
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self, a, b):
        print(self.a + self.b)


obj = Calculator(1, 2)
obj.sum(2, 3)

