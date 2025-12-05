def check_products(range_list, product_ids):
    fresh = []
    unfresh = []

    for product_id in product_ids:
        
        #grab ranges where range_max > product_id
        plausible = [range for range in range_list if int(range[1]) >= int(product_id)]

        #then check those ranges to see if range_min < product_id
        confirmed = [range for range in plausible if int(range[0]) <= int(product_id)]

        if len(confirmed):
            fresh.append(product_id)
        else:
            unfresh.append(product_id)

    return fresh, unfresh

def range_merge(range_list):

    merged = [range_list[0]]

    for range in range_list[1:]:
        #make sure the range is either absorbed into another range
        #or else it becomes it's own range in merged
        absorbed = False
        for index, merged_range in enumerate(merged):
            range_min, range_max = int(range[0]), int(range[1])
            merge_min, merge_max = int(merged_range[0]), int(merged_range[1])

            if merge_min >= range_min and merge_max <= range_max:
                #this range encompasses the merged range
                #replace it!
                print("subsuming")
                merged[index] = range
                absorbed=True
            elif merge_min <= range_min and merge_max >= range_min:
                #this range starts within the merged range...
                if range_max > merge_max:
                    #and the range has a bigger maximum!
                    print("pushing right", range, merged_range)
                    #push the boundary right
                    merged[index][1] = range_max
                absorbed = True
            elif merge_min <= range_max and merge_max >= range_max:
                #this range has a maximum within the merged range
                if range_min < merge_min:
                    #and the range has a smaller minimum!
                    print("pushing left", range, merged_range)
                    #push the boundary left
                    merged[index][0] = range_min
                absorbed = True
        if not absorbed:
            #this range is distinct
            merged.append(range)

    #unique results only!
    uniques = []
    for range in merged:
        if range not in uniques:
            uniques.append(range)

    if len(uniques) != len(merged):
        print("there really were duplicate ranges")
 
    return uniques

if __name__ == "__main__":

    #read in input
    with open("9-input.txt", "r") as f:
        data = f.read()
    
    ranges, products = data.split("\n\n")
    ranges = [range.split("-") for range in ranges.split("\n")]
    products = products.split("\n")[:-1] #knock off that final \n

    merged = range_merge(ranges)

    
    while ranges != merged:
        ranges = merged
        merged = range_merge(merged)

        if ranges == merged:
            print("stability reached")

    fresh = 0
    for range in merged:
        diff = int(range[1]) - int(range[0]) + 1
        fresh += diff

    print(fresh)
