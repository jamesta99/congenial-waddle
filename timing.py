import time
def calculate_time(func):
	def wrapper():
		start_time = time.time()
		func()
		print("Total time: ", time.time() - start_time)
	return wrapper

def fizzbuzz():
	print("Fizzbuzz")

fizzbuzz = calculate_time(fizzbuzz)
