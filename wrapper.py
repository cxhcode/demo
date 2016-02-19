import time
import functools


def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("call function: %s and %s" % (func.__name__, text))
            func1 = func(*args, **kwargs)
            print("after")
            return func1

        return wrapper

    return decorator


@log("execute")
def now():
    print(time.localtime())


@log()
def hehe():
    print(time.localtime())


now()
hehe()
