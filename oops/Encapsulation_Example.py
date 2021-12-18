class Base:
    def __init__(self):
        self._a = 2
        self.__b = 3

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Derived class")
        print(self._a)

d = Derived()
print(d._a)

d2 = Base()
print(d2._a)
print(d2.__b) # In this line will get Excpetion (AttributeError) because __b variable scope is private