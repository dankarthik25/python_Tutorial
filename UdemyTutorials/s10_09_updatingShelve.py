import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes') as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta" ] = pasta
    # recipes["soup"] = soup

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
# # We see the recipes is not updates the problem is the butter,tomato are saved in db
# #     but recipes does not know that it is updates

# # there are two ways

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    for snack in recipes:
        print(snack, recipes[snack])

# # method 2:
with shelve.open('recipes', writeback=True) as recipes:
    recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])

# writeback caches obj in memory and does not update write the dir and use the syn method
# if we close the shelve it will take a time because it need to write all the data in memory at once
# disadvanges is memory usage
# syn disadvanges
# syn cause all the data in caches to memory but also clear the caches
