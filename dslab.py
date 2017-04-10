def manipulate_date(type_, data):
	if type_ == 'list':
		return data[::-1]

	if type_ == 'set':
		add = {'ANDELA', 'TIA', 'AFRICA'}
		return data.union(add)

	if type_ == 'dictionary':
		return data.keys()

print manipulate_date('dictionary', {1 : 'v', 2: 'd', 3:'w'})


