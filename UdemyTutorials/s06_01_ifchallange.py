name = input("Enter your name ")
x1 = int (input("{} enter your age".format(name)))
print(x1)
# print((age >= 18) and (age <= 31))
if 18<=x1<=31:
	print("Your are eligible for holidays ")
else:
	print("Your age is above 31 you are uneligible for applying holidays ")