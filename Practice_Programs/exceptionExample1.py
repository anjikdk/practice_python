class exceptionExample1:

    def test(self):
        try:
            print("try")
            i = 10/0
            print(i)
        
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except ArithmeticError:
            print("ArithmeticError")
        finally:
            print("finally")

e = exceptionExample1()
#e.test()
