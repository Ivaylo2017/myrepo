def integer():
	i = int(input("Please enter an integer: "))
	if i<=0:
		print("Invalid input.")
		i = int(input("Please enter an integer: "))
	if i%2==0:
		print(i, "is even")
	else:
		print(i, "is odd")

integer()