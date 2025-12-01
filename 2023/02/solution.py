file = open("input.txt", "r")
lines = file.read().splitlines()

def calculate_min_cubes(all_games_string):
    game_strings = all_games_string.split(';')
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    for game_string in game_strings:
        cube_draws = game_string.split(',')

        for cube_draw in cube_draws:
            cube_count_string, cube_type_string = tuple(cube_draw.strip().split(' '))
            cube_count = int(cube_count_string)
            cube_type = cube_type_string.strip()

            if (min_cubes[cube_type] < cube_count):
                min_cubes[cube_type] = cube_count

    return min_cubes

def is_valid_game(min_cubes):
    return min_cubes["red"] <= 12 and min_cubes["green"] <= 13 and min_cubes["blue"] <= 14

sum_of_valid_games = 0
sum_of_power = 0

for line in lines:
    game_id_string, all_games_string = tuple(line.split(':'))
    game_id = int(game_id_string[5:])

    min_cubes = calculate_min_cubes(all_games_string)
    if (is_valid_game(min_cubes)):
        sum_of_valid_games += game_id
    sum_of_power += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

print(sum_of_valid_games)
print(sum_of_power)
