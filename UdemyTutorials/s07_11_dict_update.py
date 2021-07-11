fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

#==================================================
#  Here .update is simillar to .sort in list databuinding is done
# =================================================

veg.update(fruit)
print("veg  after update :")
print( veg)

print(fruit.update(veg))
print("fruit after update : ")
print(fruit)


###########################################################
#  To make a dict with out changing the current dict is
###########################################################

frutiNveg = fruit.copy()
frutiNveg.update(veg)
print(frutiNveg)
print(veg)
print(fruit)