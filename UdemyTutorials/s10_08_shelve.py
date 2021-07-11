# pickle drawback all obj to be loaded to memory
#   For large file loading is not sutable

# like dic it hold key value pairs  that can be pickled
# ================================================================
#
# import shelve
#
# with shelve.open("shelfTest") as fruit:
#     fruit["orange"]= "a sweet,orange,citrus"
#     fruit["apple"] = "good for making cider"
#     fruit["lemon"] = "a sour,yellow"
#     fruit["grape"] = "a summer fruit"
#     print (fruit)
#     print (fruit["orange"])
#
#
#
# print (fruit)
# ================================================================
# Result
# a sweet,orange,citrus
# a summer fruit
# <shelve.DbfilenameShelf object at 0x7f54fa2b61d0>

# print (fruit["grape"])# runing this fill give error because fruits can be only be acessed inside the with block
# ===========================================================================

import shelve


fruit= shelve.open("shelfTest")
fruit["orange"]= "a sweet,orange,citrus"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour,yellow"
fruit["grape"] = "a summer fruit"
for i in fruit:
    print (i +" : "+fruit[i])

# print (fruit["orange"])

fruit.close()

print (fruit)


#  =============================
#
#       Updating Shelves
#
# ===========================

fruit = shelve.open("shelfTest")
fruit['lime'] = 'indian fruits '
#  we can update the files

print ("After updating lime")
for i in fruit:
    print (i +" : "+fruit[i])

print (fruit.values())
print (fruit.items())

print ("List of items are ")
for v in fruit.items():
    print ( v )
print ("List of values are ")
for v in fruit.values():
    print ( v )

fruit.close()

# dic vs shelve ?
# shelve key  must be string but dic can be int