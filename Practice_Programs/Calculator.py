class Calculator:

    i = 10
    j = 20

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def add(self, a, b):
        print(a+b)

    @staticmethod
    def add1(a, b):
        print(a+b)
    
c = Calculator(5, 6)
c.add(2, 5)

Calculator.add1(20, 30)