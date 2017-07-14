from queue import Queue
from functools import wraps

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inline_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
