from functools import reduce


def str2float(s):
    def struct(s):
        return s.split(".")
    def str2num(L):
        return int(L)
    def sum(x, y):
        n = len(str(y))
        return x+(y/pow(10,n))
    x = struct(s)
    print(x)

    i = list(map(str2num, struct(s)))
    print(i)

    return reduce(sum, i)

print(str2float('123.456'))

