import time
def calculate_time(func):
	'''Decorator that prints the time it takes for a function func to execute'''
	def wrapper():
		'''Wrapper that contains the implementation of the decorator'''
		start_time = time.time()
		func()
		print("Total time: ", time.time() - start_time)
	return wrapper

def fizzbuzz():
	print("Fizzbuzz")

fizzbuzz = calculate_time(fizzbuzz)
