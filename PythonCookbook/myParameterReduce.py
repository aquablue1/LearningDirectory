from functools import partial
import math


def spam(a, b, c, d):
    print(a, b, c, d)


def test1():
    s1 = partial(spam, 1)  # a = 1
    s1(2,3,4)
    s1(4,5,6)
    s2 = partial(spam, d=42)
    s2(2,3,4)
    s2(4,5,6)
    s3 = partial(spam, 1, 2, d=42)
    s3(3)
    s3(5)


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)


def test2():
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    pt = (4, 3)
    points.sort(key=partial(distance, pt)) # sort based on the return value of distance
    print(points)

if __name__ == '__main__':
    # test1()
    test2()
