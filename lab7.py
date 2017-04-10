'''
You are presented with two arrays, all containing positive integers. 
One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77
'''

def find_missing(x, y):
	if type(x) and type(y) == list:
		if len(x) == 0 and len(y) == 0:
			return 0

		else:
			t = set(y). issubset(set(x))
			if t == True:
				return 0
			return list(set(y).difference(set(x)))
	else:
		return 'enter two lists!'


print find_missing([1, 2, 3], [1, 2, 3, 4])