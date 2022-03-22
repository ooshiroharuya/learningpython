import time
from functools import wraps


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s' % func.__name__)
        return func

    return wrapper()


def new_log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@new_log('execute')
def now():
    print('2015-3-25')


def power(num):
    return pow(num, 2)


# def hi(name='yasoob'):
#     print('now you are inside the hi() function')
#
#     def greet():
#         return 'now you are in the greet() function'
#
#     def welcome():
#         return 'now you are in the welcome() function'
#
#     print(greet())
#     print(welcome())
#     print('now you are back in the hi() function')

# def hi(name='yasoob'):
#     def greet():
#         return 'now you are in the greet() function'
#     def welcome():
#         return 'now you are in the welcome() function'
#
#     if name == 'yasoob':
#         return greet
#     else:
#         return welcome

def hi():
    return 'hi, yasoob!'


def doSomethingBeforehi(func):
    print('I am doing some boring work before executing hi()')
    print(func())


# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print('i am doing some boring work before executing a_func')
#
#         a_func()
#
#         print('I am doing some boring work after executing a_func()')
#
#     return wrapTheFunction

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('i am doing some boring work before executing a_func()')
        a_func()
        print('I am doing some boring work after executing a_func()')

    return wrapTheFunction


@a_new_decorator
def a_function_requring_decoration():
    print("I am the function which needs more decoration to remove my foul smell")


# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run"
#         return f(*args, **kwargs)
#     return decorated


# can_run = True
# print(func())
#
# can_run = False
# print(func())

# def logit(func):
#     # @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#     return with_logging

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


# @logit()
# def addition_func(x):
#     """Do some math."""
#     return x + x


@logit()
def myfunc1():
    pass


@logit(logfile='myfunc2.log')
def myfunc2():
    pass

def metric(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        print('%s executed in %s ms' % (func.__name__, time.time()))
        return func(*args, **kwargs)
    return wrapped_function

def _private_1(name):
    return "Hello, %s!" % name

def _private_2(name):
    return "Hi %s!" % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)