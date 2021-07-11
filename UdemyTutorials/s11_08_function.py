def python_food():
    print("spam and eggs")

#  python should have two blank line after fun definition
# def center_text(text):
#     left_margin = (80-len(text))//2
#     print (" "*left_margin,text)
#
# # parametrs are the variables defined in function defination
# # arg is actuall value that use to call ex: spam adn eggs , spam spam and eggs
#
# print(python_food())
# center_text("spam and eggs")
# center_text("spam, spam and eggs")
# center_text("spam, spam, spam and spam")

#=======================================================================================
#
# def center_text(*args):
#     text = ""
#     for arg in args:
#         text += str(arg)+ " "
#     left_margin = (80-len(text))//2
#     print (" "*left_margin,text)

# # print(python_food())
# center_text("spam and eggs")
# center_text("spam, spam and eggs")
# center_text("spam, spam, spam and spam")
#
#
# center_text("first", 3,5,"second")
#


def center_text(*args, c_sep='',c_end="\n", c_file=None, c_flush=False):
    text = ""
    for arg in args:
        text += str(arg)+ c_sep
    left_margin = (80-len(text))//2
    print (" "*left_margin,text,end = c_end, file=c_file,flush=c_flush)

# # parametrs are the variables defined in function defination
# # arg is actuall value that use to call ex: spam adn eggs , spam spam and eggs
#
# print(python_food())
center_text("spam and eggs")
center_text("spam, spam and eggs")
center_text("spam, spam, spam and spam")


center_text("first", 3,5,"second",3,4,"spam",c_sep=" : ")