
if __name__ == "__main__":

    with open("13-input.txt", "r") as f:
        TACHYONS = [list(line.strip()) for line in f.readlines()]

    #create a list of possible worlds per index
    incoming = [1 if beam == "S" else 0 for loc, beam in enumerate(TACHYONS[0])]
    outgoing = [0] * len(TACHYONS[0])

    for row, setup in enumerate(TACHYONS[1:]):

        #identify indices where the world lines will encounter a beam splitter
        apparatus = { loc for loc, app in enumerate(setup) if app == "^" }

        outgoing = list(incoming)

        #first remove the outgoing signal where a splitter is in front of it 
        for loc in apparatus:
            outgoing[loc] = 0
        
        #now handle the beams resulting from the splitters
        for loc in apparatus:
            #now that we're not using a set we need to be careful with boundaries
            if loc >=0 and loc <= len(setup) and incoming[loc]:
                outgoing[loc-1] = outgoing[loc-1] + incoming[loc]
                outgoing[loc+1] = outgoing[loc+1] + incoming[loc]

        incoming = outgoing


    print(outgoing)
    print(sum(outgoing)) 
