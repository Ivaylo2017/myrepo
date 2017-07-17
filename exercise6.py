def pattern():
	for i in range(9):
		if i < 5:
			print("*" * (i+1))
		else:
			print("*" * (9-i))
pattern()