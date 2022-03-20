from functools import reduce


def power(x, n=2):
    s = 1
    while n > 1:
        n -= 1
        s *= x
    return s

def enroll(name, gender):
    print('name: ', name)
    print('gender', gender)

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for i in numbers:
        sum += power(i, i)
    return sum

def mul(*args):

    if None is args or len(args) == 0:
        raise TypeError("不可以为空")

    x = 1
    for i in args:
        if not isinstance(i, (int, float)):
            raise TypeError('输入有误，必须为数字')
        x *= i
    return x

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def move(n, a, b, c):
    if n  == 1:
        print('move', a, '-->' ,c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

def findMinAndMax(L):
    minNum = None
    maxNum = None

    if len(L) == 0:
        return maxNum, minNum

    for value, x in enumerate(L):
        if 0 == value:
            maxNum = x
            minNum = x
        else:
            if x > maxNum:
                maxNum = x
            if x < minNum:
                minNum = x

    return maxNum, minNum

def normalize(name):
    return str(name[0]).upper() + str(name[1:]).lower()

def prod(L):
    def justdoit(x1, x2):
        return x1 * x2

    return reduce(justdoit, L)

def str2float(s):
    s = s.split(".")
    big_num = s[0]
    short_num = s[1]

    def bigNum(s1, s2):
        i1 = int(s1)
        i2 = int(s2)

        return s1*10 + s2

    i1 = reduce(bigNum, big_num)

def by_name(t):
    return t[0]

def count():
    def f(j):
        def g():
            return j * j
        return g()
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

def log(func):
    def wrapper(*args, **kwargs):
        print('call %s(): ' % func.__name__)
        return func(*args, **kwargs)
    return wrapper()

@log
def now():
    print("2021-03-19")
