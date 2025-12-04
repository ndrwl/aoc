file = open("input.txt", "r")
lines = file.read().splitlines()
lines = [list(line) for line in lines]

roll_char = '@'
blank_char = '.'

def is_roll(x, y):
    global lines, roll_char
    if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[0]):
        return False
    return lines[x][y] == roll_char

def count_neighbors(x, y):
    global lines
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if is_roll(x + dx, y + dy):
                count += 1
    return count

forkliftable = 0

for x in range(len(lines)):
    for y in range(len(lines[0])):
        if is_roll(x, y) and count_neighbors(x, y) < 4:
            forkliftable += 1

print("Initially forkliftable rolls: %d" % forkliftable)

forkliftable = 0
removed_any = True

while removed_any:
    removed_any = False
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if is_roll(x, y) and count_neighbors(x, y) < 4:
                lines[x][y] = blank_char
                removed_any = True
                forkliftable += 1

print("Eventually forkliftable rolls: %d" % forkliftable)