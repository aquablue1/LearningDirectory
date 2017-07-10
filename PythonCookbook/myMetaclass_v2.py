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

    def __init__(self):
        print("use test init")


if __name__ == '__main__':
    print("bad")
    ut = useTest()