# ###############################333
#
#  if elif and else
#
####################################

# Ex for if


# name  = input("Please enter your name ")
# age = int(input("How old are you {0}".format(name)))
#
# print(age)
#
# # if age>= 18:
# if (age >= 16) and (age <=65):
# # if 16 <= age<= 65:
# # if 17< age<66:
# if (age < 16):
# 	#  != not equal,	 == equal, 		< less, 		> greater,	 <= less than equal, 	>= greater than equal
# 	print("You are not eligible to vote Come back after {0} years".format(18-age))
# elif (age > 16) and (age < 66 ):
# 	print("You are eligible to vote")
# elif age >=66:
# 	print("You are eligible to vote and retired from work")
# else :
# 	print("Enter age in whole no")



if True:
	print("if allow True")

x = 12
if x:
	print("if allow int ")
else:
	print("if not allow int")


x = 12.65
if x:
	print("if allow float ")
else:
	print("if not allow float")

x = "it is string"
if x:
	print("if allow string ")
else:
	print("if not allow string")

if False:
	print("if allow False")
else:
	print("if not allow False")

x = None
if x:
	print("if allow None ")
else:
	print("if not allow None")

print(not False)
print(not True)
