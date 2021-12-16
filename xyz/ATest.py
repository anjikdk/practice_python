import sys
sys.path.append('./abc')

from A import *

class ATest:

    def test1(self):
        print("test1 method")

a = A()
a.test(10, 20)