# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

# create a function to handle loopong through the list
def loop_grid(list, index):
	line = ''
	for i in range(len(list)):
		line += grid[i][index]
	return line
# call the function on the grid and print according to index
print(loop_grid(grid, 0))
print(loop_grid(grid, 1))
print(loop_grid(grid, 2))
print(loop_grid(grid, 3))
print(loop_grid(grid, 4))
print(loop_grid(grid, 5))

# print('\n'.join(map(''.join, zip(*grid)))) this gives the same output