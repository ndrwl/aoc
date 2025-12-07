file = open("input.txt", "r")
lines = file.read().splitlines()

def safe_int(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    return int(s)

def try_get_number(lines, col):
    number = 0
    any_number = False

    for row in range(len(lines) - 1):
        if col < 0 or col >= len(lines[row]):
            continue
        if lines[row][col] == ' ':
            continue
        number = number * 10 + safe_int(lines[row][col])
        any_number = True

    return any_number, number

def get_symbol(lines, col):
    if col < 0 or col >= len(lines[-1]):
        return ''
    return lines[-1][col]

max_col = max(len(lines[col]) for col in range(len(lines)))

total = 0
sub_total = 0
current_operator = '*'

for col in range(max_col + 1):
    symbol = get_symbol(lines, col)

    if symbol == '*':
        current_operator = '*'
        sub_total = 1
    elif symbol == '+':
        current_operator = '+'
        sub_total = 0

    has_number, number = try_get_number(lines, col)
    if not has_number:
        total += sub_total
        sub_total = 0
        current_operator = ''
    elif current_operator == '*':
        sub_total *= number
    elif current_operator == '+':
        sub_total += number

print("Total result: %d" % total)