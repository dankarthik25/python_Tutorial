#              Converting a list to str

mylist = ["a", "b","c","d"]
newString = ""
#
for c in mylist:
		newString = c + "."			# #  OR

		# newString = ".".join(mylist)

print(newString)
newString1 = ".".join(mylist)
print(newString1)

# ===================================================================================
