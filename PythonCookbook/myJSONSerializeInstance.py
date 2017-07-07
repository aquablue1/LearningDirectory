import json

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print((self.x, self.y))

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

# Dictionary mapping names to known classes
classes = {
    'Point' : Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


if __name__ == '__main__':
    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)

    a = json.loads(s, object_hook=unserialize_object)
    print(a.y)

