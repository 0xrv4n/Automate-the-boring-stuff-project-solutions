def printTable(val):
	col_widths = [0] * len(val)
	num = 0
	while num < len(val):
		for i in val[num]:
			if len(i) > col_widths[num]:
				col_widths[num] = len(i)

		num +=1

	for word in range(len(val[0])):
		for item in range(len(val)):
			print(val[item][word].rjust(col_widths[item]), end=' ')
		print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

printTable(table_data)