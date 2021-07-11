# # Closures:
# # Wiki: a closure is a record storing a function[a] together with an environmentself.
# The environment is a mapping associating each free variable of the function
# (variables that are used locally, but defined in an enclosing scope)
# with the value or reference to which the name was bound when the closure was created.
#
# Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references,
# even when the function is invoked outside their scope.

#
# def outer_func():
#     message = 'HI'
#
#     def inner_func():
#         print(message)
#     return inner_func
#
#
# my_func = outer_func()
# print(my_func.__name__)
# my_func()
# my_func()


# def outer_func(msg):
#     message = msg
#
#     def inner_func():
#         print(message)
#     return inner_func
#
#
# hi_func = outer_func('Hi')
# hello_func = outer_func('Hello')
# bey_func = outer_func('bey')
# hi_func()
# hello_func()
# bey_func()


def outer_func
