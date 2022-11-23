def fib(number):
    f0 = 0
    f1 = 1

    for i in range(number+1):
        yield f0
        t = f0
        f0 = f1
        f1 = t + f1


for i in fib(20):
    print(i)