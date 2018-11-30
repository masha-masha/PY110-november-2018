import datetime
import time

############################################
# NotATask: training

"""
def decor(func):
    def wrap(*args, **kwargs):
        wrap.count += 1
        print(datetime.datetime.now())
        print("this function is called " + str(wrap.count) + " times")
        print("Name of the function is " + func.__name__)
        res = func(*args, **kwargs)
        return res
    wrap.count = 0
    return wrap


@decor
def f():
    time.sleep(1)

f()
f()
f()
"""

############################################
# first task: print evaluation time

"""
def decor(f):
    def wrap(*arg, **kwargs):
        start = time.perf_counter()
        res = f(*arg, **kwargs)
        print("Eval Time: " + str(time.perf_counter() - start))
        return res
    return wrap

@decor
def func():
    time.sleep(1)
"""

############################################
# second task: decor + cache

"""
def convert(arg, dict):
    res = list()
    for x in arg:
        res.append(x)
    for x in dict:
        res.append(x[0])
        res.append(x[1])

    return tuple(res)


def decor(f):
    def wrap(*arg, **kwargs):
        start = time.perf_counter()
        # res = 0
        arkw = convert(arg, kwargs)
        if len(wrap.dict) != 0:
            value = wrap.dict.get(arkw)
            if value is None:
                res = f(*arg, **kwargs)
            else:
                # wrap.dict[key] = value
                res = value
        else:
            res = f(*arg, **kwargs)
        wrap.dict.update({arkw: res})
        print("Eval Time: " + str(time.perf_counter() - start))
        print(wrap.dict)
        return res
    wrap.dict = {}
    return wrap


@decor
def func(a, b):
    time.sleep(1)
    return a + b


func(1, 2)

func(1, 2)
func(1, 3)
func(1, 3)
"""

# third task: compare evaluation time of native and cachable fibonacci versions


def convert(arg, dict):
    res = list()
    for x in arg:
        res.append(x)
    dict = sorted(dict.items(), key=lambda x: x[0], reverse=True)
    for x in dict:
        res.append(x[0])
        res.append(x[1])

    return tuple(res)


def decor(f):
    def wrap(*arg, **kwargs):
        arkw = convert(arg, kwargs)
        if len(wrap.dict) != 0:
            value = wrap.dict.get(arkw)
            if value is None:
                res = f(*arg, **kwargs)
            else:
                res = value
        else:
            res = f(*arg, **kwargs)
        wrap.dict.update({arkw: res})
        return res
    wrap.dict = {}
    return wrap


def fib0(a):
    assert(a >= 1)
    assert(type(a) is int)
    if a > 2:
        return fib0(a-1) + fib0(a-2)
    elif 1 <= a <= 2:
        return 1


time_ = time.perf_counter()
fib0(30)
time_ = time.perf_counter() - time_
print("Native fibonacci # 30 time: " + str(time_))
time_ = time.perf_counter()
fib0(35)
time_ = time.perf_counter() - time_
print("Native fibonacci # 50 time: " + str(time_))

fib0 = decor(fib0)

time_ = time.perf_counter()
fib0(30)
time_ = time.perf_counter() - time_
print("Cachable fibonacci # 30 time: " + str(time_))
time_ = time.perf_counter()
fib0(35)
time_ = time.perf_counter() - time_
print("Cachable fibonacci # 50 time: " + str(time_))

#fib0(-1)
