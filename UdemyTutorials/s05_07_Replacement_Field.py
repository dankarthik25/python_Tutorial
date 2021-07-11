
#  Precision using old formating version
for i in range(1, 12):
    print("No. {0:4} square is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
# {1:4} ,  {2:4}   printing is in order :	 Space and then follwed by Floting No.


for i in range(1, 12):
    print("No. {0:4} square is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
# {1:<4} , {2:<4}  printing is in order :	 Floting No. followed by space


print( "Pi value is appox {0:12.30}".format(22/7) )
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:53.50f}".format(22 / 7))
print("Pi is approximately {0:54.50f}".format(22 / 7))
print("Pi is approximately {0:55.50f}".format(22 / 7))
print("Pi is approximately {0:56.50f}".format(22 / 7))


for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

