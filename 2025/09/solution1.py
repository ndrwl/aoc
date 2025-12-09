file = open("input.txt", "r")
lines = file.read().splitlines()

coordinates = [[int(x_str) for x_str in line.split(",")] for line in lines]

def calculate_is_clockwise(coordinates):
    total = 0
    for i in range(len(coordinates)):
        j = (i + 1) % len(coordinates)
        total += (coordinates[j][0] - coordinates[i][0]) * (coordinates[j][1] + coordinates[i][1])
    return total < 0

def is_interior(pre_corner, corner, post_corner, query, is_clockwise):
    corner_test = (corner[0] - pre_corner[0]) * (post_corner[1] - corner[1]) - (corner[1] - pre_corner[1]) * (post_corner[0] - corner[0])
    is_interior_corner = is_clockwise == (corner_test >= 0)

    pre_corner_test = (corner[0] - pre_corner[0]) * (query[1] - pre_corner[1]) - (corner[1] - pre_corner[1]) * (query[0] - pre_corner[0])
    is_inside_pre = is_clockwise == (pre_corner_test >= 0)

    post_corner_test = (post_corner[0] - corner[0]) * (query[1] - corner[1]) - (post_corner[1] - corner[1]) * (query[0] - corner[0])
    is_inside_post = is_clockwise == (post_corner_test >= 0)

    if is_interior_corner:
        return is_inside_pre and is_inside_post
    else:
        return is_inside_pre or is_inside_post

def is_valid_pair(coordinates, i, j, is_clockwise):
    if not is_interior(coordinates[i - 1], coordinates[i], coordinates[(i + 1) % len(coordinates)], coordinates[j], is_clockwise):
        return False
    if not is_interior(coordinates[j - 1], coordinates[j], coordinates[(j + 1) % len(coordinates)], coordinates[i], is_clockwise):
        return False

    max_x = max(coordinates[i][0], coordinates[j][0])
    min_x = min(coordinates[i][0], coordinates[j][0])
    max_y = max(coordinates[i][1], coordinates[j][1])
    min_y = min(coordinates[i][1], coordinates[j][1])

    for k in range(len(coordinates)):
        if k == i or k == j:
            continue

        other = coordinates[k]

        is_inside_x = min_x < other[0] < max_x
        is_inside_y = min_y < other[1] < max_y

        if is_inside_x and is_inside_y:
            return False

        other_edge = coordinates[(k + 1) % len(coordinates)]

        if is_inside_x and min_x < other_edge[0] < max_x:
            if other[1] < min_y and other_edge[1] > max_y:
                return False
            if other[1] > max_y and other_edge[1] < min_y:
                return False
        if is_inside_y and min_y < other_edge[1] < max_y:
            if other[0] < min_x and other_edge[0] > max_x:
                return False
            if other[0] > max_x and other_edge[0] < min_x:
                return False

    return True

is_clockwise = calculate_is_clockwise(coordinates)

max_area_all = 0
max_area_restricted = 0

for i in range(len(coordinates)):
    for j in range(i):
        area = (abs(coordinates[i][0] - coordinates[j][0]) + 1) * (abs(coordinates[i][1] - coordinates[j][1]) + 1)
        if area > max_area_all:
            max_area_all = area

        if is_valid_pair(coordinates, i, j, is_clockwise):
            if area > max_area_restricted:
                max_area_restricted = area

print("Max area for all pairs: %d" % max_area_all)
print("Max area for valid pairs: %d" % max_area_restricted)