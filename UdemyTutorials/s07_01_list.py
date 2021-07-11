# # List iniciallization
#
# list_1 = []			# empty list
# list_2 = list()		# empty list
#
# ###############################
# 	# Data Binding
# ###############################
#
# even1  = [2, 4, 6, 8]
# even2 = even1		# >>> even2 is even1		>>> True
#
# print(even2 is even1)
# even2.sort(reverse=True)
# print(even)
# # Changes done in even2 will change even1 vic versa, this is called Data Binding
#
#
#
#
# x1= [1,2,3,4,5,6,90,1,54,78,6,34]
# print(x1)
# x1.sort() # .sort doestnot create a new list (obj) but change the existing list
# print(x1)
#

l1 = ['Screenshot from 2018-10-29 19-06-37.png', 'Screenshot from 2018-10-29 19-06-23.png', 'Screenshot from 2018-11-25 17-12-24.png', 'Screenshot from 2018-10-29 19-09-23.png', 'Screenshot from 2018-11-10 11-27-37.png', 'Screenshot from 2018-10-29 19-05-50.png', 'Screenshot from 2018-11-03 10-36-19.png']

print ("\n -".join(l1))