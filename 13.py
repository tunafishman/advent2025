
if __name__ == "__main__":

	with open("13-input.txt", "r") as f:
		TACHYONS = [list(line.strip()) for line in f.readlines()]

	incoming = set([loc for loc, beam in enumerate(TACHYONS[0]) if beam == "S"])

	total_splits = 0

	for row, splitter in enumerate(TACHYONS[1:]):
		print(" -- {} -- ".format(row))
		apparatus = { loc for loc, app in enumerate(splitter) if app == "^" }
		outgoing = incoming

		#first remove the outgoing signal where a splitter is in front of it 
		outgoing = outgoing.difference(apparatus)
		
		total_splits += (len(incoming) - len(outgoing))

		#now handle the beams resulting from the splitters
		for loc in apparatus:
			outgoing.update({loc-1, loc+1})

		print("in", incoming)
		print("app", apparatus)
		print("out", outgoing)

		incoming = outgoing


	print(total_splits)
 
