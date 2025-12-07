from collections import defaultdict

file = open("input.txt", "r")
lines = file.read().splitlines()

current_beam = {lines[0].index('S') : 1}
current_index = 2
splits = 0

while current_index < len(lines):
    new_beam = defaultdict(int)

    for pos in current_beam:
        if lines[current_index][pos] == '^':
            new_beam[pos + 1] += current_beam[pos]
            new_beam[pos - 1] += current_beam[pos]
            splits += 1
        else:
            new_beam[pos] += current_beam[pos]

    current_beam = new_beam
    current_index += 2

print("Number of splits: %d" % splits)
print("Number of timelines: %d" % sum(current_beam.values()))