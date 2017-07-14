

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

if __name__ == '__main__':
    apply_async(add, (2, 3), callback=print_result)

    r = ResultHandler()
    apply_async(add, (2, 3), callback=r.handler)
    apply_async(add, ("hello", "world"), callback=r.handler)

    handler = make_handler()
    apply_async(add, (2,3), callback=handler)