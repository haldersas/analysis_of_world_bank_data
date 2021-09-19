def nth_power(n, fn = lambda x: x**2):
	"""
	calculates power for numbers upto n
	"""

	return [fn(i) for i in range(n)]

print(nth_power(10))


# def nth_power(n, power):
# 	"""
# 	calculates power for numbers upto n
# 	"""

# 	return [i**power for i in range(n)]

# print(nth_power(10,4))