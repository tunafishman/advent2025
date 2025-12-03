def max_concat(battery_bank, num_digits):

    
    #find the maximum value in the battery_bank such that you leave enough in the array to make a
    #joltage with num_digits
    
    #always you must leave the space
    digit_range = len(battery_bank) - (num_digits-1)
    usable_battery=battery_bank[:digit_range]
    
    biggest = max(usable_battery)

    #where is it's first occurrence in the list?
    index = battery_bank.index(biggest) + 1

    if num_digits > 1:
        return biggest * 10 ** (num_digits-1) + max_concat(battery_bank[index:], num_digits-1)
        
    else:
        return biggest 

    

if __name__ == "__main__":

    #read input

    with open("5-input.txt", "r") as f:
        battery_banks = f.readlines()

    joltages = []

    for bank in battery_banks:
        joltages.append(max_concat([int(x) for x in bank.strip()], 12))

    print(sum(joltages))
