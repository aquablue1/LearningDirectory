# test the execute sequence of meataclass.

class test(type):
    def __init__(self, clsname, bases, clsdict):
        print("good")

class practice(type):
    print("practice")

class childTest(metaclass=test):
    def __init__(self):
        print("child Test")


class useTest(childTest):
    print("use test")

    def __init__(self, name=""):
        self.name = name
        print("use test init")

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.name = value

class getTest():
    ut = useTest("bob")

if __name__ == '__main__':
    print("bad")
    print(getTest.ut)