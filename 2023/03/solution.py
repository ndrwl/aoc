file = open("input.txt", "r")
lines = file.read().splitlines()

sum = 0
gears = {}

def is_part(row, start_col, end_col):
    global lines
    for r in range(max(0, row - 1), min(len(lines), row + 2)):
        for c in range(max(0, start_col - 1), min(len(lines[0]), end_col + 1)):
            if (lines[r][c] != '.' and not lines[r][c].isnumeric()):
                return True
    return False

def mark_gears(row, start_col, end_col, number):
    global lines, gears
    for r in range(max(0, row - 1), min(len(lines), row + 2)):
        for c in range(max(0, start_col - 1), min(len(lines[0]), end_col + 1)):
            if (lines[r][c] == '*'):
                gears.setdefault((r,c), [])
                gears[(r,c)].append(number)

for row, line in enumerate(lines):
    is_in_number = False
    start_col = 0

    for col, char in enumerate(line + "."):
        if (not char.isnumeric()):
            if (is_in_number):
                number = int(line[start_col:col])
                if (is_part(row, start_col, col)):
                    sum += number
                mark_gears(row, start_col, col, number)
            is_in_number = False
        else:
            if (not is_in_number):
                is_in_number = True
                start_col = col

print(sum)

gear_sum = 0
for v in gears.values():
    if (len(v) == 2):
        gear_sum += v[0] * v[1]
print(gear_sum)
