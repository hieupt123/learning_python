# decorator
import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print(f'{time.time() - t1} s')
        return result
    return wrapper


def generator_function(num):
    for i in range(num):
        yield i*2

result = generator_function(100)
# print('1 next: ', next(result))
# print('2 next: ', next(result))
# print('3 next: ', next(result))

# for i in generator_function(100):
#     print(i)

@performance
def long_time(num):
    print('1')
    for i in range(num):
        i*2

@performance
def long_time2(num):
    print('2')
    for i in list(range(num)):
        i*2

num = 100000000
long_time(num)
long_time2(num)


