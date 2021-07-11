# jabber = open("/home/dan/Downloads/sample.txt","r")
#
# for line in jabber:
# 	if "jabberwock" in line.lower():
# 		print(line, end="")				# here end='' has no use '.' line as \n
#
# jabber.close()		# Here file should be colsed after use or else it will be corrupted

# with open("/home/dan/Downloads/sample.txt",'r') as jabber:
# 	for line in jabber:
# 		print(line,end='')

# with open("/home/dan/Downloads/sample.txt","r") as jabber:
# 	line = jabber.read()
# 	while line:
# 		print(line,end='')
# 		line = jabber.readlines()

# with open("/home/dan/Downloads/sample.txt",'r') as jabber:
# 	lines = jabber.readlines()
# 	print(lines)

# # here \n is added at end of line all lines in single line
# for line in lines:
# 	print(line,end='')


with open("/home/dan/Downloads/sample.txt",'r') as jabber:
	lines = jabber.read()
for line in lines[::-1]:
	print(line,end='')


