# DECORATORS

# CLOJERS, 1st class funtions : functions are treated as variables
# Decorators


# #########################33
# CLOJERS, 1st Class Functions:
# return's  a exe function
# #######################


def outer_func():
    message = 'HI'
# free variable : message var is not def, call but can acess the outer function variable

    def inner_func():
        print(message)
    return inner_func()


outer_func()        # HI


# #############################
# CLOJERS, 1st Class Functions:
# return's  a function waiting for execution
# ######################################3333


def outer_func():
    message = 'HI'
# free variable : message var is not def, call but can acess the outer function variable

    def inner_func():
        print(message)
    return inner_func


my_func = outer_func()
print(my_func.__name__)
my_func()
my_func()

# #############################
# CLOJERS, 1st Class Functions:
# passing a variable`
# return's  a function waiting for execution
# ######################################3333


def outer_func(msg):
    def inner_func():
        print(message)
    return inner_func


my_func = outer_func()
print(my_func.__name__)
my_func()
my_func()

# ###########################
# What is decorator ? :
# Decorator is a function that take another function  as arg and add  some functionallity and return  the function  without changing the source code of original function
# 1st Class Vs Decorator : insted of passing a var(msg) we pass a function(original_func)
# ###############################


def decorator_function(original_func):
    def wrapper_function():
        # we can add functionallity without changing the source code
        return original_func()
    return wrapper_function


def display():
    print('dispaly function ran')


# set (decorator_dispaly var) to decorator_function passed display(function)
# then the original_func is display function
# then created a wrapper function
# return a wrapper function waiting to be executed
# when wrapper function is executed  then  original function is executed
decorator_dispaly = decorator_function(display)
decorator_dispaly()     # wrapper function is executed then execute the original function (display)


# ###########################
# Decorator function syntax with NO-ARGUMENTS
# ###############################


def decorator_function(original_func):
    def wrapper_function():
        # we can add functionallity without changing the source code
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func()
    return wrapper_function


@decorator_function
def display():
    print('dispaly function ran')


# dispaly = decorator_function(display) # No need to write
display()

# ###########################
# Decorator function syntax with ARGUMENTS
# ###############################


def decorator_function(original_func):
    def wrapper_function():
        # we can add functionallity without changing the source code
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func()
    return wrapper_function


# ###########################
# Decorator function syntax with NO-ARGUMENTS
# ###############################


def decorator_function(original_func):
    def wrapper_function(*args, **kwargs):
        # we can add functionallity without changing the source code
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('dispaly function ran')


@decorator_function
def display_info(name, age):
    print('dispaly function ran with argument ({}, {})'.format(name, age))


display()
display_info('John', 35)


# ###########################
# ClassDecorator  syntax with ARGUMENTS
# ###############################

class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('call method execute this before {}'.format(self.original_func.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('dispaly function ran')


@decorator_class
def display_info(name, age):
    print('dispaly function ran with argument ({}, {})'.format(name, age))


display()
display_info('John', 35)


# ###########################
# Practical Example : logging
# ###############################


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print('dispaly function ran with argument ({}, {})'.format(name, age))


display()
display_info('John', 35)


# ###########################
# Practical Example : timing
# ###############################


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Tom', 22)


display()
display_info('John', 35)

# ###########################
# Practical Example : logging and timing
# ###############################


# import time
# from functools import wraps       # wraps is used to not changig origina function
#
#
# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
#
#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)
#
#     return wrapper
#
#
# def my_timer(orig_func):
#     import time
#
#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result
#
#     return wrapper
#
#
# @my_logger
# @my_timer         #  means : display_info = my_logger(my_timer(display_info))
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('Tom', 22)
