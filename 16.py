def dist_sq(coord1, coord2):

    return sum( (int(coord1[i]) - int(coord2[i]))**2 for i in [0, 1, 2])

def next_min(connections_matrix):
    
    min = connections_matrix[0][0]
    i, j = 0, 0
    for m, dists in enumerate(connections_matrix):
        for n, dist in enumerate(dists):
            if dist != -1 and dist < min:
                min = connections_matrix[m][n]
                i, j = m, n
                
    return i, j

def next_mins_easy(connections_matrix, limit=0):

    distances = []
    for i, row in enumerate(connections_matrix):
        for j, entry in enumerate(row):
            distances.append((i, i+1+j, entry))

    distances.sort(key=lambda item: item[2])

    if limit:
        return distances[:limit]
    else:
        return distances

def circuit_coalesce(circuits, new_circ=set()):

    if len(new_circ) != 0:
        circuits.append(new_circ)

    ret_circuits = [circuits[0]]

    for existing_circ in circuits[1:]:
        found = False
        for index, already_found in enumerate(ret_circuits):

            if len(existing_circ & already_found) > 0:
                
                ret_circuits[index].update(existing_circ)
                found = True
                break
            
        if not found:
            ret_circuits.append(existing_circ)


    #we may have redundant circuits if we just made a new one
    if len(new_circ) != 0:
        ret_circuits = circuit_coalesce(ret_circuits)

    return(ret_circuits)

def is_sub_circuit(circuits, new_circ):
    
    sub = False

    for circ in circuits:
        if new_circ.issubset(circ):
            sub=True

    return sub

if __name__ == "__main__":

    #with open("15-sample.txt", "r")  as f:
    with open("15-input.txt", "r")  as f:
        jxns = [line.strip().split(",") for line in f.readlines()]

    everything = []

    for m in range(len(jxns)-1):
        everything.append([])
        for n in range(m+1, len(jxns)):
            dist = dist_sq(jxns[m],jxns[n])

            #this puts a distance at the nth index of the mth row
            #which corresponds to the connection of
            #junction m and junction n+(m+1) 
            everything[m].append(dist)

    circuits=[{x} for x in range(len(jxns))]
    print(len(circuits))
    connection_num = 0
    #max_connections = 1000

    distances = next_mins_easy(everything)
    
    while len(circuits) > 1: 

        #c1, c2 = next_min(everything)
        connection = distances[connection_num]
        c1, c2 = connection[0], connection[1]
        new_node_set = {c1, c2}

        #this thing is tricky.
        #upper triangular, zero indexed matrix means that index j of the list in row i
        #is actually the i+j+1 node in the original input list. Ugh.
        #new_node_set = {c1, (c1+1)+c2}

        #check whether these two nodes are already connected in a circuit
        if not is_sub_circuit(circuits, new_node_set):
            circuits = circuit_coalesce(circuits, new_node_set)
        
        #mark this connection between junctions as handled
        #everything[c1][c2] = -1

        connection_num+=1 

    print(int(jxns[c1][0]) * int(jxns[c2][0]))

