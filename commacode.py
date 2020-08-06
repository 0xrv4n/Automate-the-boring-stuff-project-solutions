def comma(list):
	# function to separate items in a list with comma and space with and before the last item
	if len(list) > 1:
		return ', '.join(list[:-1]) + ' and ' + list[-1]+'.'
	# If list item is > 1 return list with comma, space with and before the last item
	else:
		return 'This is not a valid list'
	# If list item isn't > 1 return 'This is not a valid list'

print(comma(['Xbox', 'Playstation', 'Nitendo', 'Mobile'])) # returns Xbox, Playstation, Nitendo and Mobile.
print(comma(['Xbox'])) # returns This is not a valid list