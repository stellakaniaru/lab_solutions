'''Function takes an argument and returns results
based on argument provided.'''

def data_type(x):
	if type(x) == None:
		return 'no value'

	elif type(x) == str:
		return len(x)

	elif type(x) == bool:
		return x

	elif type(x) == list:
		if len(x) >= 3:
			return x[2]
		return None

	elif type(x) == int:
		if x == 100:
			return 'equal to 100'
		elif x < 100:
			return 'less than 100'
		else:
			return 'more than 100'

print data_type(None)

