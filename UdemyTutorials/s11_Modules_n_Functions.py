# import turtle   import all modules

# from turtle import forward, right, circle,done
# this is used only when single modules is repetedly  used


done = "Well done you have finished the drawing "
from turtle import *
# import everything  which is not recommented
# reason is u dont know what is imported and which may lead to hide the data

# done is over writen



done = "Well done, you have finished your drawing"

forward(150)
right(250)
forward(150)
circle(75)

done()
print(done)