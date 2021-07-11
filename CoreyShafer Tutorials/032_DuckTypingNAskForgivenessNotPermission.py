# 032_DuckTypingN
# Easier to AskForgiveness than not Permission (EAFP)


# class Duck:
#
#     def quack(self):
#         print('Quack, quack')

#     def fly(self):
#         print('Flap, Flap')


# class Person:
#     def quack(self):
#         print("I'm Quacking like a Duck")

#     def fly(self):
#         print('I\' Flapping my Arms')


# def quack_and_fly(thing):
#     # Duck Typing (We don't care what that type of obj but only care what it can do when we ask )
#     # This can be dangourous but we use some check by (Non Pythonic : (LBYL)Look Befor You Leavue  ) or (Pythonic:)
#     thing.quack()
#     thing.fly()
#
#
# # # ##############################
#     # (LBYL)Look Befor You Leave
#####################################
# def quack_and_fly(thing):
#     # Not Duck-Typed (Non-Pythonic)

#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.fly()
#
#
# def quack_and_fly(thing):
#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)
#     print()
#
#
# d = Duck()
# quack_and_fly(d)
#
# p = Person()
# quack_and_fly(p)
#


##############################
# Example
# 333
#
# # person = {'name': "Jess", 'age': 23, 'job': 'Programmer'}
# person = {'name': "Jess", 'age': 23}
#
# # LBYL (Non-Pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print("I'm{name}. I'm {age} years old and I am a {job}".format(**person))
# else:
#     print('Missing some keys')
#
# # EAFP
# try:
#     print("I'm{name}. I'm {age} years old and I am a {job}".format(**person))
# except KeyError as e:
#     print('Missing {} keys'.format(e))


# 33
# Example by list
##########################

# my_list = [1.2, 3, 4, 5, 6]
#
# # Non-Pythonic
#
# if len(my_list) > 6:
#     print(my_list[5])
# else:
#     print('That index does not exist')
#
# # Pythonic
# try:
#     print(my_list[5])
# except IndexError:
#     print('That index does not exist')
#
#
# # Why we use EAFP is good thing:(Easier to Ask Forgiveness than not Permission (EAFP))
# # - Faster (to asking obj one time)
# # - More Readable
# # -


##############################
# Race the Condtion
##############################

import os

my_file = "/tmp/text.txt"

# Race Condition
if os.acess(my_file, os.R_Ok):          # if can acess file
    # during time btw if cond and acess file may be we can't acess the file
    with open(my_file) as f:
        print(f.read())
else:
    print('File can not be accessed')

# No Race Condition

try:
    f = open(my_file)           # try to acess file
except IOError as e:            # if not
    print('File can not be accessed')
else:  # if no error  then exe below code
    with f:
        print(f.read())
