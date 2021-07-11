# print (dir())
#
# for i in dir(_builtins__):
#     print(dir(i))
#
#
#


import shelve
#  to view sourve code on shelve press Control over shelve
print (dir())

for i in dir(shelve):
    print (i)
print ("methods in Shelve")
for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print (obj)


