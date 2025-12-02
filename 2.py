import os
import sys

def move_dial(initial_position, movement):

    direction, amount = movement[:1], int(movement[1:])

    print("Starting at:", initial_position)

    effective_amount = amount % 100
    revolutions = amount // 100

    print("Moving {} in {} direction".format(amount, direction))
    print("but really that's just {} rotations and then {} moves".format(revolutions, effective_amount))

    final_position = initial_position - effective_amount if direction == "L" else initial_position + effective_amount 

    clicks = abs(revolutions)
    
    if final_position < 0 and initial_position != 0: #if we started at 0, then we didn't click when we first turned left
        clicks += 1
        print("left of zero", final_position, initial_position)

    if final_position > 100:
        clicks += 1
        print("bigger than 100")

    final_position = final_position % 100

    if final_position == 0 and initial_position !=0:
        clicks +=1
        print("landed on zero")

    print(initial_position, final_position, amount, direction, clicks)
    return final_position, clicks

def make_moves(initial_position, list_of_moves):

    current_position = initial_position
    password = 0

    for move in list_of_moves:
        final_position, clicks = move_dial(current_position, move)

        current_position = final_position
        password += clicks

    return password


if __name__ == "__main__":

    if sys.argv[1] and os.path.isfile(sys.argv[1]):
        move_file = sys.argv[1]
    else:
        print("specify a list of moves file as an argument")
        exit()

    with open(move_file, "r") as f:
        list_of_moves = f.readlines()

    #initialize dial
    current_position = 50
    zeroes = 0

    password = make_moves(current_position, list_of_moves)

    print(password)
