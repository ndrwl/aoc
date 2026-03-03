file = open("input.txt", "r")
lines = file.read().splitlines()

galaxies = []

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            galaxies.append((i, j))

def expand_galaxies(galaxies, expansion_size = 2):
    rows_with_galaxies = list({ galaxy[0] for galaxy in galaxies })
    rows_with_galaxies.sort()
    columns_with_galaxies = list({ galaxy[1] for galaxy in galaxies })
    columns_with_galaxies.sort()

    expanded_row_mapping = {}
    expanded_column_mapping = {}

    for i in range(len(rows_with_galaxies)):
        expanded_row_mapping[rows_with_galaxies[i]] = rows_with_galaxies[i] + (rows_with_galaxies[i] - i) * (expansion_size - 1)
    for i in range(len(columns_with_galaxies)):
        expanded_column_mapping[columns_with_galaxies[i]] = columns_with_galaxies[i] + (columns_with_galaxies[i] - i) * (expansion_size - 1)

    return [(expanded_row_mapping[galaxy[0]], expanded_column_mapping[galaxy[1]]) for galaxy in galaxies]

def calculate_total_distance(galaxies):
    total_distance = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            galaxy1 = galaxies[i]
            galaxy2 = galaxies[j]

            total_distance += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    return total_distance

galaxies_normal_expansion = expand_galaxies(galaxies, 2)
galaxies_million_expansion = expand_galaxies(galaxies, 1000000)

print(calculate_total_distance(galaxies_normal_expansion))
print(calculate_total_distance(galaxies_million_expansion))