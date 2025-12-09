file = open("input.txt", "r")
lines = file.read().splitlines()

seeds = [int(x) for x in lines[0][lines[0].index(":")+1:].strip().split(" ")]

maps = []

for line in lines[1:]:
    if line.strip() == "":
        continue
    if line.endswith("map:"):
        maps.append([])
        continue

    maps[-1].append([int(x) for x in line.strip().split(" ")])

def map_value(value, mapx):
    for new_val, old_val, range in mapx:
        if value >= old_val and value <= old_val + range:
            return new_val + (value - old_val)
    return value

def map_seed(seed, maps):
    value = seed
    for mapx in maps:
        value = map_value(value, mapx)
    return value

print("Min location: %d" % min([map_seed(seed, maps) for seed in seeds]))