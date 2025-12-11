




#with open("17-sample.txt", "r") as f:
with open("17-input.txt", "r") as f:
    coords =[(int(x[0]), int(x[1])) for x in [line.strip().split(",") for line in f.readlines()]]

#build another upper triangular matric
full_list = []

for m, coord in enumerate(coords):
    for n, opposite_corner in enumerate(coords[m+1:]):
        print(coord, opposite_corner)
        area = (1+abs(coord[0] - opposite_corner[0])) * (1+abs(coord[1] - opposite_corner[1]))

        full_list.append((m, m+1+n, area))

full_list.sort(key=lambda info: info[2], reverse=True)

print(full_list[0])
