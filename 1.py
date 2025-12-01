import sys

DIAL = list(range(0, 100))

def move_dial(current_position, movement):

    direction, amount = movement[:1], int(movement[1:])

    if direction == "L":
        # move left
        index = (current_position - amount) % 100
    else:
        index = (current_position + amount) % 100

    print(index)
    final_position = DIAL[index]
    print(final_position)

    return final_position

def run_program(initial_position, list_of_moves):

    current_position = initial_position
    password = 0

    for movement in list_of_moves:
        current_position = move_dial(current_position, movement)

        if current_position == 0:
            password+=1

    return password

if __name__ == "__main__":

    move_file = sys.argv[1]

    with open(move_file, "r") as f:
        list_of_moves = f.readlines()

    password = run_program(50, list_of_moves)

    print("PASSWORD IS: {}".format(password)) 
