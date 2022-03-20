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