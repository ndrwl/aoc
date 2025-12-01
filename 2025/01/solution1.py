from operator import floordiv

file = open("input.txt", "r")
lines = file.read().splitlines()

def text_to_turn_value(text):
    value = int(text[1:])
    if text.startswith("L"):
        return -value
    return value

revolutions = 100
position = 50
count_zero = 0
count_zero_any = 0

for line in lines:
    delta = text_to_turn_value(line)

    if position == 0 and delta < 0:
        position += revolutions

    position += delta

    if position >= revolutions:
        count_zero_any += position // revolutions
    elif position <= 0:
        count_zero_any -= (position - 1) // revolutions

    position %= revolutions

    if position == 0:
        count_zero += 1

print("Times landed on zero: %d" % count_zero)
print("Times past zero: %d" % count_zero_any)
