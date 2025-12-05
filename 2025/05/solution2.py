file = open("input.txt", "r")
lines = file.read().splitlines()

split_idx = lines.index('')

ranges = []

def add_range(ranges, new_start, new_end):
    range_idx = 0
    while range_idx < len(ranges):
        start, end = ranges[range_idx]
        if new_end < start or new_start > end:
            range_idx += 1
        else:
            new_start = min(new_start, start)
            new_end = max(new_end, end)
            ranges.pop(range_idx)
    ranges.append((new_start, new_end))

for range_str in lines[:split_idx]:
    parts = range_str.split("-")
    start = int(parts[0])
    end = int(parts[1])
    add_range(ranges, start, end)

num_ingredients = 0

for start, end in ranges:
    num_ingredients += end - start + 1

print("Number of fresh ingredients: %d" % num_ingredients)