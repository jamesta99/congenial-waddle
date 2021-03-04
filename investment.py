def calculate_apr(principal, interest_rate, years):
	'''Calculates the APR of an investment given the principal amount, the interest rate, and the time in years'''
	apr = 0.0
	if principal < 0 or interest_rate < 0 or years < 1:
		return False
	apr = principal*(1+interest_rate)**years
	return apr

