from functools import wraps
import time


def timeme(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        time1 = time.clock()
        f(*args, **kwargs)
        time2 = time.clock()
        print(f'It took {(time2 - time1)*1000} ms to complete {f.__name__}')
    return wrapper

@timeme
def myfunc():
    """ My function to sleep"""
    time.sleep(1)
    print("Inside myfunc")


myfunc()
print(myfunc.__doc__)
