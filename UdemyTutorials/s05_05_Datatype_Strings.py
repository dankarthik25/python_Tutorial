##########################
#   Data Type Sequence : Strings
#############################
s ='hello world'  # >> s =  'hello world'
# >> s[3] = 'l', s[0] =  'h', s[-1] = 'd', s[0:6] = 'hello '
# >>> s[:6]
# 'hello '
# >>> s[6:]
# 'world'
# >>> s[-5:]
# 'world'
# >>> s[0:11:2]
# 'hlowrd'
# >>> s[1:11:2]
# 'el ol'
# >>> s[::2]
# 'hlowrd'



#############################3#
#   String Formating
###############################

age = 24
print("My age is " + str(age) + "year")				# >>> My age is 24 year


##########################################
#
#   Replacement field
#
######################################


print("My age is {0} years".format(age)) 								# >>> My age is 24 years

print("I am {0} years, {1} mounts, {2} days old".format(28,4,19))		# >>> I am 28 years, 4 mounts, 19 days old

print("""
 January     :{2} days
 February    :{0} days
 March       :{1} days
 April       :{1} days
 May         :{2} days
 June        :{1} days
 July        :{2} days
 August      :{2} days
 September   :{1} days
 October     :{2} days
 November    :{1} days
 December    :{2} days""".format(28, 30, 31))

# >>>
# January     :31 days
# February    :28 days
# March       :30 days
# April       :30 days
# May         :31 days
# June        :30 days
# July        :31 days
# August      :31 days
# September   :30 days
# October     :31 days
# November    :30 days
# December    :31 days

# Formating Operator used in python 2 and no longer used in python3


