#  Generator does't all values hold the memory
# It does't show any difference in small value but for
# Large list or data it will it will reduce memory and increase performace


# def square_nums(nums):
#     result = []
#     for i in nums:
#         # print(i * i)
#         result.append(i * i)
#     return result
#
# #######################33
# List Comprehension
# ###########################3
# my_nums = [x*x for x in [1,2,3,4,5]]
# print my_nums            # [1,2,3,4,5]

#  ########################
# Using Generator
# #############################


# # # def square_nums(nums):
# # #     for i in nums:
# # #         # print(i * i)
# # #         yield(i * i)
# # #
# # #
# # # my_nums = square_nums([1, 2, 3, 4, 5])
# # # # The above method can be implemented by list compression
# # my_nums = [x * x for x in [1, 2, 3, 4, 5]]    # list compression
# # # The above method can be used as generator
# my_nums = (x * x for x in [1, 2, 3, 4, 5])    # p
# print (my_nums)            # generator object square_num at 0x1004d
#
# # for num in my_nums:
# #     print (num)
#
# # to read all values from generator (by conerting to list)
#
# print(list(my_nums)) # (lose adv of performace)


# #################################3
# list Vs Generator
# Generator : not all held in memory so has high performace if size  large

# ##############################
# Example: For Memory and Performace difference
# 33

import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before):{}Mb'.format(mem_profile.memory_usauge_resource()))


def people_list(num_people):
    result = []
    for i in range(num_pople):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
        return result


def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.clock()
people = people_list(10**6)
# people = people_generator(10**6)
t2 = time.clock()

print
print('Memory (After):{}Mb'.format(mem_profile.memory_usauge_resource()))
print ('Took {} Second'.format(t2 - t1))
