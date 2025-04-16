#file name: calculator

import math_tools

def calc():
	num1 = float(input("enter the first number: "))
	num2 = float(input("enter the second number: "))
	
	operation = input("Choose an operation (add,subtract, multiple, divide: ").strip().lower()

	if operation == 'add':
		result = math.tools.add(num1, num2)
	elif operation == 'subtract':
		result = math.tools.subtract(num1, num2)
	elif operation == 'multiply':
		result = math.tools.multiply(num1, num2)
	elif operation == 'divide':
		result = math.tools.divide(num1, num2)
	else:
		print('pick one of the options')
		return
	print (f'Result: {result}')
 
if __name__ == "__calc__":
	calc()
