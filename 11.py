from functools import reduce

if __name__ == "__main__":

	with open("11-input.txt", "r") as f:
		maths = f.readlines()

	maths = [line.split() for line in maths]

	columns = []

	for i in range(len(maths[0])):
		#temp_column = []
		#for row in range(len(maths)):
		#	print(row, i)
		#	temp_column.append(maths[row][i])
		columns.append([maths[row][i] for row in range(len(maths))])
		#print(temp_column)
		#columns.append(temp_column)

	final_sum = 0

	for col in columns:
		if col[4] == "*":
			final_sum+=reduce(lambda x, y: int(x) * int(y), col[:4])
		elif col[4] == "+":
			final_sum+=reduce(lambda x, y: int(x) + int(y), col[:4])

	print(final_sum)
