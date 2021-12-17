import traceback

def test():
    try:
        print("try")
        a = 0
        b = 10
        c = b/a
        print(c)
    except:
        print("Exception occured")
    finally:
        print("finally")

    print("end of the program")
test()
