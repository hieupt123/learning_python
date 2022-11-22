# Decorator

import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        print(f'time {time.time() - t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i+1

long_time()