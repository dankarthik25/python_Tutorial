
#############################

# String Formating Operator (no longer used in python 3  )

#############################
age = 24
print("My age is %d years using string formationg " %age) 								# >>> My age is 24 years




for i in range(1, 12):
    print("No. %2d square is %4d and cubed is %4d" %(i, i ** 2, i ** 3))		# >>> %d %2d, %4d  rightspace before var respectively #

# >>>

# No.  1 square is    1 and cubed is    1
# No.  2 square is    4 and cubed is    8
# No.  3 square is    9 and cubed is   27
# No.  4 square is   16 and cubed is   64
# No.  5 square is   25 and cubed is  125
# No.  6 square is   36 and cubed is  216
# No.  7 square is   49 and cubed is  343
# No.  8 square is   64 and cubed is  512
# No.  9 square is   81 and cubed is  729
# No. 10 square is  100 and cubed is 1000
# No. 11 square is  121 and cubed is 1331

###########################################################

# %12.50f >> If 12> 50 ==>size = 12  (RightSpace.s + Number.s + Point.s +  DecimalNAumber(precision).s

#############################################################
#                                                      S = RS+N+P+DN
print("\n")
print("Pi value is appox %12f" %(22/7))    		# 12 = 04+1+1+06	>>> Pi value is appox     3.142857
print("\n")

print("		Precision is varied %12.[01-10]f and result is below ")
print("Pi value is appox %12.1f" %(22/7))    		# 12 = 09+1+1+01 	>>> Pi value is appox          3.1
print("Pi value is appox %12.2f" %(22/7))    		# 12 = 08+1+1+02 	>>> Pi value is appox         3.14
print("Pi value is appox %12.3f" %(22/7))    		# 12 = 07+1+1+03 	>>> Pi value is appox        3.143
print("Pi value is appox %12.4f" %(22/7))    		# 12 = 06+1+1+04 	>>> Pi value is appox       3.1429
print("Pi value is appox %12.5f" %(22/7))    		# 12 = 05+1+1+05 	>>> Pi value is appox      3.14286
print("Pi value is appox %12.6f" %(22/7))    		# 12 = 04+1+1+06 	>>> Pi value is appox     3.142857
print("Pi value is appox %12.7f" %(22/7))    		# 12 = 03+1+1+07 	>>> Pi value is appox    3.1428571
print("Pi value is appox %12.8f" %(22/7))    		# 12 = 02+1+1+08 	>>> Pi value is appox   3.14285714
print("Pi value is appox %12.9f" %(22/7))    		# 12 = 01+1+1+09 	>>> Pi value is appox  3.142857143
print("Pi value is appox %12.10f" %(22/7))    		# 12 = 00+1+1+10 	>>> Pi value is appox 3.1428571429
print("		Conclusion :%12f used for left indexing by 12 spaces only if size No. is less than 12")
print("\n")


print("		Precission >  Left Indexing then  ")


print("Pi value is appox %12.11f" %(22/7))    		# 13 = 00+1+1+11 	>>> Pi value is appox 3.14285714286
print("Pi value is appox %12.12f" %(22/7))    		# 14 = 00+1+1+12 	>>> Pi value is appox 3.142857142857
print("Pi value is appox %12.13f" %(22/7))    		# 15 = 00+1+1+13 	>>> Pi value is appox 3.1428571428571
print("Pi value is appox %12.14f" %(22/7))    		# 16 = 00+1+1+14 	>>> Pi value is appox 3.14285714285714
print("Pi value is appox %12.15f" %(22/7))    		# 17 = 00+1+1+15 	>>> Pi value is appox 3.142857142857143
print("Pi value is appox %12.16f" %(22/7))    		# 18 = 00+1+1+16 	>>> Pi value is appox 3.1428571428571428
print("Pi value is appox %12.17f" %(22/7))    		# 19 = 00+1+1+17 	>>> Pi value is appox 3.14285714285714279
print("Pi value is appox %12.18f" %(22/7))    		# 20 = 00+1+1+18 	>>> Pi value is appox 3.142857142857142794
print("Pi value is appox %12.19f" %(22/7))    		# 21 = 00+1+1+19 	>>> Pi value is appox 3.1428571428571427937
print("Pi value is appox %12.20f" %(22/7))    		# 22 = 00+1+1+20 	>>> Pi value is appox 3.14285714285714279370

print("Pi value is appox %12.30f" %(22/7))    		# 23 = 00+1+1+30 	>>> Pi value is appox 3.142857142857142793701541449991
print("Pi value is appox %12.40f" %(22/7))    		# 24 = 00+1+1+40 	>>> Pi value is appox 3.1428571428571427937015414499910548329353
print("Pi value is appox %12.50f" %(22/7))    		# 25 = 00+1+1+50 	>>> Pi value is appox 3.14285714285714279370154144999105483293533325195312
print("		Conclusion :If precision > Right space then no right shift is done")
print("\n")

print("Pi value is appox %11f" %(22/7))       		# 11 = 03+1+1+06 	>>> Pi value is appox    3.142857
print("Pi value is appox %10f" %(22/7))       		# 10 = 02+1+1+06 	>>> Pi value is appox   3.142857
print("Pi value is appox %9f" %(22/7))       		# 09 = 01+1+1+06 	>>> Pi value is appox  3.142857
print("Pi value is appox %8f" %(22/7))			# 09 = 00+1+1+06 	>>> Pi value is appox 3.142857
print("Pi value is appox %7f" %(22/7))			# 09 = 00+1+1+06 	>>> Pi value is appox 3.142857
print("Pi value is appox %6f" %(22/7))			# 09 = 00+1+1+06 	>>> Pi value is appox 3.142857
print("		Conclusion :By Default Precission is 6digits")


