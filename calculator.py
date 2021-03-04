def calculator(number1, number2, operator):
	'''Recieves two numbers and an operator, then performs an operation using both numbers
and the operator. Prints the result afterwards'''
	if operator == "+":
		answer = number1 + number2
	elif operator == "-":
		answer = number1 - number2
	elif operator == "*":
		answer = number1 * number2
	elif operator == "/":
		answer = number1 / number2
	elif operator == "//":
		answer = number1 // number2
	elif operator == "**":
		answer = number1 ** number2
	else:
		sys.exit("Invalid operation")
	print(answer)

def input_output():
	'''Function for evaluating simple expressions. Asks the user for two numbers and an operator, then passes 
them to the calculator function for evaluation. After the answer is printed, asks the user to continue or not'''
	number1 = float(input("Enter the first number: "))
	number2 = float(input("Enter the second number: "))
	operator = input("Enter the operation: ")
	calculator(number1, number2, operator)
	terminate = input("Do you wish to exit? ")
	if terminate == "n":
		input_output()
	elif terminate == "y":
		sys.exit("Program ended")
