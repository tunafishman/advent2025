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

def pattern_generate(start, end, palindromes_only = False):
    
    patterns = []

    num_digits = len(start)
    if palindromes_only: #let a user recover only specific patterns (palindromes)
        if num_digits % 2 == 0:
            factors = [int(num_digits/2)]
        else:
            return patterns 
    else: #discover all
        factors = [i for i in range(1, num_digits+1) if num_digits % i == 0 and i < num_digits]

    for factor in factors:
        #find repeated patterns

            first_chunk_floor = start[:factor]
            first_chunk_ceiling = end[:factor]

            #generate all possible palindromes based on possible first chunks
            possible_pats = [ str(chunk)*(int(num_digits/factor)) for chunk in range(int(first_chunk_floor), int(first_chunk_ceiling)+1)]

            #only keep the possible palindromes that fit witnin the given range
            reasonable_pats = list(filter(lambda x: int(x)>=int(start) and int(x)<=int(end), possible_pats))

            patterns.extend(reasonable_pats)

    return patterns

def pattern_finder(start, end, palindromes=False):

    pats = []

    #divide range into subrange blocks to assure constant number of digits in integer   
    for block in subranges(start, end):
        pats.extend(pattern_generate(block[0], block[1], [] if not palindromes else [2]))

    return pats


if __name__ == "__main__":

    #open ID ranges and parse them

    with open("3-ranges.txt", "r") as f:
        ranges = f.readline().strip("\n").split(",")
    
    parsed_ranges = [{"start":item[0], "end":item[1]} for item in [thing.split("-") for thing in ranges]]

    global_patterns = []
    for block in parsed_ranges:
        global_patterns.extend(pattern_finder(block["start"], block["end"], palindromes=False))

    #apprently there are duplicates in these ranges now! Overlapping!
    deduped = set(global_patterns)

    print("grand total", sum([int(x) for x in deduped]))
