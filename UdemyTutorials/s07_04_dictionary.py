fruit = {"orange": "a sweet, orange, citrus fruit",
	 "apple" : "good for making cider",
	 "lemon" : "a sour, yellow citrus fruit",
	 "grape" : "a small, sweet fruit growing in bunches",
	 "lime"  : "a sour, green citrus fruit"}
# ====================================
#  Adding a new key to existing Dic
print(fruit)
	# >>> {'apple': 'good for making cider', 'lemon': 'a sour, yellow citrus fruit', 'orange': 'a sweet, orange, citrus fruit', 'grape': 'a small, sweet fruit growing in bunches', 'lime': 'a sour, green citrus fruit'}
fruit["pear"] = "an odd shaped apple"
print(fruit)
# >>> {'apple': 'good for making cider', 'pear': 'an odd shaped apple', 'orange': 'a sweet, orange, citrus fruit', 'lime': 'a sour, green citrus fruit', 'grape': 'a small, sweet fruit growing in bunches', 'lemon': 'a sour, yellow citrus fruit'}
# =====================================
# 	Updating or Replacing existing key
fruit["lime"] = "great with tequila"
print(fruit)
# =====================================
# #   Deleting a key,value from Dic
# del fruit["lemon"]
# =====================================
# # Deleting a Dic
# del fruit
# =====================================
# # 	Emptying the Dictionary
# fruit.clear()
# print(fruit)
# =====================================


while True:
	dict_key = input("Please enter a fruit: ")
	if dict_key == "quit":
		break
	description = fruit.get(dict_key, "We don't have a" + dict_key)
	print(description)
	# if dict_key in fruit:
	# 	description = fruit.get(dict_key)
	# 	print(description)
	# else:
	# 	print("we don't have a " + dict_key)
# =========================================
#  Every time we run we will get different order

for item in fruit :
	print( item + "is"+ fruit[item])



# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f  + " - " + fruit[f])
# for val in fruit.values():
#     print(val)
#
# print('-' * 40)
#
# for key in fruit:
#     print(fruit[key])

fruit_keys = fruit.keys()
print(fruit_keys)

fruit_list = fruit.items() 			# Convert dic to list containing tuples ( key, value )
# [('lime', 'a sour, green citrus fruit'), ('apple', 'good for making cider') .....etc ]

fruit_tup = tuple(fruit.items()) 	# Convert dic to tuples containing tuples (key, value)
# (  ('lime', 'a sour, green citrus fruit'), ('apple', 'good for making cider') .....etc )

fruit_dic2 = dict( fruit_tup)		# Convert tuple to dic
