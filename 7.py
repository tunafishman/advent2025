def neighbor_generator(i, j):

	# coordinates above, below, left and right of given i, j

	neighbor_list = [ (i-1, j-1), (i-1, j), (i-1, j+1),
					  ( i , j-1),           ( i , j+1),
					  (i+1, j-1), (i+1, j), (i+1, j+1) ]
	
	return neighbor_list

def accessible_rolls(abstract_data):

	accessibles = []
	for coordinate in abstract_data:
		coordinate_neighbors = neighbor_generator(coordinate[0], coordinate[1])

		if sum([1 for x in coordinate_neighbors if x in abstract_data]) < 4:
			accessibles.append(coordinate)

	return accessibles
		
def abstracted(full_grid):
	#take a full grid and return a list of sets of paper roll coordinates

	abstract_rows = set()
	for row, roll_map in enumerate(full_grid):
		for column, symbol in enumerate(list(roll_map)):
			print("row", row, "column", column, "symbol", symbol)
			if symbol == "@":
				abstract_rows.add((row, column))

	return abstract_rows

	

if __name__ == "__main__":
	
	#read in input

	with open("7-input.txt", "r") as f:
		paper_rolls = f.readlines()

	row_data = abstracted(paper_rolls)

	print(sum([1 for x in accessible_rolls(row_data)]))

