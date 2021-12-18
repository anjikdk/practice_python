class Base:
    def add(self, a, b):
        return a+b

class Derived(Base):
    def sub(self, a, b):
        return a-b


d = Derived()
print(d.add(10, 20))