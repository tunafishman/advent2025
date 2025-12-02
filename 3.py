#within given ranges, find "product IDs" that appear as tidy palindromes

# IDs must first be an even number of digits

def subranges(start, end):
	
	#divide initial ranges into subranges based on number of digits

	subranges = []
	
	#first check if start and end have different lengths

	if len(start) == len(end):

		subranges.append((start, end))

	else: # (1 - 15) -> [(1-9), (10-15)] eg

		lens = range(len(start), len(end)+1)

		for n in lens:

			floor = str(10 ** (n-1)) if 10 ** (n-1) > int(start) else start
			ceiling = "9"*n if int("9"*n) < int(end) else end
		
			subranges.append((floor, ceiling))

	return subranges

def palindrome_finder(start, end):

	pals = []
	
	print("checking range {} - {}".format(start, end))
	#divide range into subrange blocks to assure constant number of digits in integer	
	for block in subranges(start, end):

		if len(block[0]) % 2:
			#odd number of digits -> no palindrome
			continue
		else:
			
			pal_repeat_len = int(len(block[0])/2)

			first_chunk_floor = block[0][:pal_repeat_len]
			first_chunk_ceiling = block[1][:pal_repeat_len]
 
			#generate all possible palindromes based on possible first chunks
			possible_pals = [ str(chunk)*2 for chunk in range(int(first_chunk_floor), int(first_chunk_ceiling)+1)]

			#only keep the possible palindromes that fit witnin the given range
			reasonable_pals = list(filter(lambda x: int(x)>=int(block[0]) and int(x)<=int(block[1]), possible_pals))

			print("reasonable", reasonable_pals)
			pals.extend(reasonable_pals)

	return pals


if __name__ == "__main__":

	#open ID ranges and parse them

	with open("3-ranges.txt", "r") as f:
		ranges = f.readline().split(",")
	
	parsed_ranges = [{"start":item[0], "end":item[1]} for item in [thing.split("-") for thing in ranges]]

	global_palindromes = []
	for block in parsed_ranges:
		global_palindromes.extend(palindrome_finder(block["start"], block["end"]))


	print(global_palindromes)
	print("grand total", sum([int(x) for x in global_palindromes]))
