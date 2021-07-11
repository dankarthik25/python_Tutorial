# Player will give the input
# "LOCATION : ROAD,BUILDING,FOREST,VALLY,HILL,QUIT" rather than
# direction "NORTH, SOUTH, EAST, WEST"

# steps
# 	Extent the input search to Location


locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
		 1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
		 2: {"N": 5, "Q": 0},
		 3: {"W": 1, "Q": 0},
		 4: {"N": 1, "W": 2, "Q": 0},
		 5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = { "Q":"QUIT",
               "N":"NORTH",
               "S": "SOUTH",
               "E": "EAST",
               "W": "WEST",
			    0: "HOME",
                1: "ROAD",
                2: "HILL",
                3: "BUILDING",
                4: "VALLEY",
                5: "FOREST" }

loc = 1


while True:
	l1 = list()
	loc_exits_ref = exits[loc].keys()

	for d in loc_exits_ref:
		l1.append( vocabulary[exits[loc][d]] + " go " + vocabulary[d]  )

	print(locations[loc])
	if loc==0:
		break
	direc = input("Avaliable direction and place are \n" + "\n".join(l1) + " ").upper()
	if len(direc)>1:
		words = direc.split()
		for w in words:
			if w in vocabulary.values():
				for key_temp, val_temp in vocabulary.items():
					if w == val_temp:
						direc = key_temp
						break
			break
	if  direc in exits[loc].keys():
		loc = exits[loc][direc]
	elif direc in exits[loc].values():
		loc = direc
	else:
		print("You cannot go in that direction")

