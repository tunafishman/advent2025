def is_inside(point, two_corners):
    
    x_range = sorted([x[0] for x in two_corners])
    y_range = sorted([y[1] for y in two_corners])
    
    is_in_x = x_range[0] < point[0] and point[0] < x_range[1]
    is_in_y = y_range[0] < point[1] and point[1] < y_range[1]

    return is_in_x and is_in_y 


def rectangle_check(corner1, corner2, grouped_perimeter):
    #somehow check if the chosen corners would create edges
    #that intersect the perimeter

    two_corners = [corner1, corner2]
    four_corners = [corner1, [corner1[0], corner2[1]], corner2, [corner2[0], corner1[1]]]

    four_sides = group_perimeter(create_perimeter(four_corners))

    valid = True
    directions = ["v", "h"]
    tests = []
    for ind, dir in enumerate(four_sides.keys()):
        #ind = 0
        #dir = "v"
        # -> opp_dir_ind = 1
        opp_dir_ind = ind ^ 1
        opp_dir = directions[opp_dir_ind]
        
        sides = four_sides[dir]
        #check intersection based on coordinate range definition of line segments
        z1, z2 = [side[ind][0] for side in sides] #the constant coordinate of each side segment
        
        #the non contstant coordinates are the same for both sides
        #because rectangle
        side_begin, side_end = sides[0][opp_dir_ind] 
        
        possible_intersectors = list(filter(lambda segment:  segment[opp_dir_ind][0] > side_begin 
            and side_end > segment[opp_dir_ind][1],
            grouped_perimeter[opp_dir]))
        
        for segment in possible_intersectors:
            perim_begin, perim_end = segment[ind]
            w = segment[opp_dir_ind][0]
        
            #a crossing rules us out 
            if ((perim_begin < z1 and z1 < perim_end) or
                (perim_begin <z2 and z2 < perim_end)):
                valid = False

            #if coincide, check other end for whether it's in rectangle interior
            elif (z1 in segment[ind] or z2 in segment[ind]):
                z = z1 if z1 in segment[ind] else z2
                coincident_point = (z, w) if ind == 0 else (w, z)

                checker = (z + 1 if z == segment[ind][0] else z - 1)
                check_point = (checker, segment[1][0]) if ind == 0 else (segment[0][0], checker)
                inside = is_inside(check_point, two_corners)
                valid = not inside 

            tests.append(valid)
            if not valid:
                break

    return all(tests) 


def create_perimeter(tile_coordinates):
    #something like [([1-5],[10,10]), ([5,5], [0,10]) ...]
    segment_list = []

    coords_num = len(tile_coordinates)

    for index in range(len((tile_coordinates))):
        c1 = tile_coordinates[index]
        c2 = tile_coordinates[(index+1) % coords_num]

        x_range = [c1[0], c2[0]]
        y_range = [c1[1], c2[1]]
        x_range.sort()
        y_range.sort()
        segment_list.append((x_range, y_range))

    return segment_list

def group_perimeter(perimeter_list): 

    grouped = {"v": [], "h": []}

    for segment in perimeter_list:
        if segment[0][0] == segment[0][1]: #constant x -> vertical
            grouped["v"].append(segment)
        else:
            grouped["h"].append(segment)

    return grouped


def generate_areas(coordinates):
    #build another upper triangular matrix
    #and return the sorted entries
    full_list = []


    for m, coord in enumerate(coordinates):
        for n, opposite_corner in enumerate(coordinates[m+1:]):
            area = (1+abs(coord[0] - opposite_corner[0])) * (1+abs(coord[1] - opposite_corner[1]))

            full_list.append((m, m+1+n, area))

    full_list.sort(key=lambda info: info[2], reverse=True)

    return full_list

#with open("17-sample.txt", "r") as f:
with open("17-input.txt", "r") as f:
    coords =[(int(x[0]), int(x[1])) for x in [line.strip().split(",") for line in f.readlines()]]

grouped_perimeter = group_perimeter(create_perimeter(coords))

possible_areas = generate_areas(coords)

for area in possible_areas:
    if rectangle_check(coords[area[0]], coords[area[1]], grouped_perimeter):
        print("Winner {}".format(area))
        break
