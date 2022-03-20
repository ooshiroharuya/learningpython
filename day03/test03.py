import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("a 不是数字类型")
    if not isinstance(b, (int, float)):
        raise TypeError("b 不是数字类型")
    if not isinstance(c, (int, float)):
        raise TypeError("c 不是数字类型")

    x1 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    x2 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)

    return x1, x2


def power(x):
    return x * x

def great_power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
