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
            if symbol == "@":
                abstract_rows.add((row, column))

    return abstract_rows

    

if __name__ == "__main__":
    
    #read in input

    with open("7-input.txt", "r") as f:
        paper_rolls = f.readlines()

    initial_row_data = abstracted(paper_rolls)

    can_get_to = accessible_rolls(initial_row_data)

    row_data = initial_row_data
    while len(can_get_to) > 0:

        row_data = set([coordinate for coordinate in row_data if coordinate not in can_get_to])
        can_get_to = accessible_rolls(row_data)

    print(len(initial_row_data) - len(row_data))  

