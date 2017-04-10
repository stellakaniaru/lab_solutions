'''
Study the pattern below and write your program to pass the tests

 phone  => pphphophonphone
 ab     => aab
 like   => lliliklike
'''


class StringSplosion(object):

	#initialize class and attributes
	def __init__(self, string):
		self.string = string



	def manipulate(self):
		#give the variable result an empty string
		result  = ""
		
		#iterate through each letter in the string
		for i in range(1, len(self.string) + 1):
			#slice after every letter and add each slice to the empty string
			result += self.string[:i]
		return result
