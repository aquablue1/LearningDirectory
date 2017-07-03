
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a+self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def add_children(self, node):
        self._children.append(node)






def fab(maxLimit):
    n, a, b = 0, 0, 1
    while n < maxLimit:
        yield b
        # print(b)
        a, b = b, a + b
        n = n + 1

if __name__ == '__main__':
    """
    for i in fab(10):
        print(i)




    a = 1
    b = 2
    b, b = b, a+b
    print(b)
    """
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    for ch in root:
        print(ch)