#file name: calculator

import math_tools

def calc():
	num1 = float(input("enter the first number: "))
	num2 = float(input("enter the second number: "))
	
	operation = input("Choose an operation (add, subtract, multiply, divide: ").strip().lower()

	if operation == 'add':
		result = math_tools.add(num1, num2)
	elif operation == 'subtract':
		result = math_tools.subtract(num1, num2)
	elif operation == 'multiply':
		result = math_tools.multiply(num1, num2)
	elif operation == 'divide':
		result = math_tools.divide(num1, num2)
	else:
		print('pick one of the options')
		return
	print (f'Result: {result}')
 
print (calc())
