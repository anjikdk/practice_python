class example1:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def test(self):
        name = input("Enter name: ")
        print(name)
        print(self.fname)

e = example1("abc", "xyz")
e.test()