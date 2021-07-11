# t,w,r,a different  modes



# For more details visit https://docs.python.org/3/library/functions.html#open
#


imelda = "More Mayhem", "Imelda MAy", "2011", (
     (1, "Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("sample.txt", 'a') as imelda_file:
    print(imelda, file=imelda_file)



#
# with open("sample.txt","a") as tables:
#     print (tables)
#     for i in range(2,13):
#         for j in range(1,13):
#         print("{1} times {0} is {2}".formate(i,j,i*j))
# print (tables)