# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats' . But your func-
# tion should be able to work with any list value passed to it.
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
