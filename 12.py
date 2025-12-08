
if __name__ == "__main__":

    with open("11-input.txt", "r") as f:
        maths = [line.rstrip("\n") for line in f.readlines()]

    #work on columns starting at right
    final_sum, index, buffer, buf_list = 0, 0, "", []

    while index < len(maths[0]):
        buffer = ""
        operator = ""
        for row in range(len(maths)): #should be 5 
            focus = maths[row][-(index+1)]

            if focus in ("+", "*"): #if operator -> operate
                buf_list.append(buffer) #catch the last buffer before the operator
                operator = focus 

                if operator == "+":
                    final_sum += sum([int(x) for x in buf_list])

                elif operator == "*":
                    prod = 1
                    for num in buf_list:
                        prod = prod * int(num)

                    final_sum += prod

                #clean up the list
                buf_list = []
                buffer = ""
            
            elif focus != " ": #if not operator and not blank -> store
                buffer += focus
 
        if buffer:
            buf_list.append(buffer)

        index += 1

    print(final_sum)
                        
    
    #print(final_sum)
