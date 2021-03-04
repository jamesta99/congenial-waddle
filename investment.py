def calculate_apr(int principal, float interest_rate, int years):
	'''Calculates the APR of an investment given the principal amount, the interest rate, and the time in years'''
	apr = 0.0
	if principal < 0 or interest_rate < 0 or years <= 0:
		return False
	for i in range (years):
		apr = principal*(1+interest_rate)
	return apr

