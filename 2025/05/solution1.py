file = open("input.txt", "r")
lines = file.read().splitlines()

split_idx = lines.index('')

ranges = []
num_fresh = 0

for range_str in lines[:split_idx]:
    parts = range_str.split("-")
    start = int(parts[0])
    end = int(parts[1])
    ranges.append((start, end))

for ingredient_str in lines[split_idx+1:]:
    ingredient = int(ingredient_str)
    for start, end in ranges:
        if start <= ingredient <= end:
            num_fresh += 1
            break

print("Number of fresh ingredients: %d" % num_fresh)