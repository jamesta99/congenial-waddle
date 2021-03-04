def calculate_apr(int principal, float interest_rate, int years):
	apr = 0.0
	if principal < 0 or interest_rate < 0 or years <= 0:		#checks for valid inputs
		return False
	interest_rate += 1
	for i in range (years):
		apr = principal * interest_rate
	return apr

