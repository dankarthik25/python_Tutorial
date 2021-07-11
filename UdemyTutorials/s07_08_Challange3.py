#  Input now is not only " N, S, E, W "
#  But input now is  a statement like " Go to North", " In South directoin " .......et




# 1 > Create another dictionary that containing ("North,South,West,East" and compare with that players  words.
# 2 > These words will be the keys, and their values will be a single letter that
# 3 > the program can use to determine which way to go.

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
         5: {"W": 2, "S": 1, "Q": 0} }


# Creating another Dictionary  for player referance

vocabulary = { "QUIT":  "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST":  "E",
               "WEST":  "W"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()

    if (len(direction)>1):
        for word in vocabulary:
            # print(" The words in vocabulary is" + word)
            if word in direction:
                direction = vocabulary[word]		# Changing " North, South, West, East " to " N, S, W, E "
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")



# for word in vocabulary:       # words are the keys inside the dictionary
#     print(word)ea