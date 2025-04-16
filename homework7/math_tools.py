 # file name: math.tools

def add(a, b): #returns the sum of a and b
	return a + b

def subtract(a, b): #returns a minus b
	return a - b

def multiply(a, b): #returns the product of a and b
	return a * b

def divide(a, b): #returns the quotient of a divided by b  
	if b == 0:
		return 'error since not divisible by zero'
	return a / b
