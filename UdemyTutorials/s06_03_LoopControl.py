str = ['i','am','a','programmer', 'in','python']
for i in str:
	print(i,end=" ")	# >>> i am a programmer in python
	if i=="a":
		continue		# >>> i am programmer in python
		# break			# >>> i am
	print("\n")
	print(i,end=" ")

