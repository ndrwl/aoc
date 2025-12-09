file = open("input.txt", "r")
lines = file.read().splitlines()

seeds = [int(x) for x in lines[0][lines[0].index(":")+1:].strip().split(" ")]
seed_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

maps = []

for line in lines[1:]:
    if line.strip() == "":
        continue
    if line.endswith("map:"):
        maps.append([])
        continue

    maps[-1].append([int(x) for x in line.strip().split(" ")])

def add_range(ranges, new_start, new_end):
    range_idx = 0
    while range_idx < len(ranges):
        start, end = ranges[range_idx]
        if new_end < start - 1 or new_start > end + 1:
            range_idx += 1
        else:
            new_start = min(new_start, start)
            new_end = max(new_end, end)
            ranges.pop(range_idx)
    ranges.append((new_start, new_end))

def map_ranges(ranges, mapx):
    new_ranges = []

    while len(ranges) > 0:
        start, end = ranges.pop(0)
        is_mapped = False

        for new_val, old_val, val_length in mapx:
            if old_val > end or old_val + val_length - 1 < start:
                continue

            map_start = max(start, old_val)
            map_end = min(end, old_val + val_length - 1)

            mapped_start = map_start - old_val + new_val
            mapped_end = map_end - old_val + new_val
            add_range(new_ranges, mapped_start, mapped_end)

            if start < old_val:
                ranges.append((start, old_val - 1))
            if end > old_val + val_length - 1:
                ranges.append((old_val + val_length, end))
            is_mapped = True
            break

        if not is_mapped:
            add_range(new_ranges, start, end)
    return new_ranges

def map_seed_ranges(seed_ranges, maps):
    ranges = seed_ranges
    for mapx in maps:
        ranges = map_ranges(ranges, mapx)
    return ranges

print("Min location: %d" % min([start for (start, end) in map_seed_ranges(seed_ranges, maps)]))