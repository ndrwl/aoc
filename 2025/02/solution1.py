file = open("input.txt", "r")
lines = file.read().splitlines()

def safe_int(s):
    if len(s) == 0:
        return 0
    return int(s)

def calculate_invalid_ids(start, end):
    end_len = len(str(end))
    ids = set()
    for parts in range(2, end_len + 1):
        ids.update(calculate_invalid_ids_by_parts(start, end, parts))
    return ids

def calculate_invalid_ids_by_parts(start, end, parts):
    ids = set()
    start_str = str(start)
    end_str = str(end)

    for length in range(len(start_str), len(end_str) + 1):
        if length % parts != 0:
            continue
        part_length = length // parts
        discard_length = length - part_length

        start_bound = max(10**(part_length - 1), safe_int(start_str[:-discard_length]))
        end_bound = min(10**part_length-1, safe_int(end_str[:-discard_length]))

        for i in range(start_bound, end_bound + 1):
            test_id = safe_int(str(i) * parts)
            if start <= test_id <= end:
                if test_id not in ids:
                    ids.add(test_id)
    return ids

total_2 = 0
total_all = 0

for line in lines:
    range_strs = line.split(",")
    for range_str in range_strs:
        parts = range_str.split("-")
        start = safe_int(parts[0])
        end = safe_int(parts[1])
        total_2 += sum(calculate_invalid_ids_by_parts(start, end, 2))
        total_all += sum(calculate_invalid_ids(start, end))

print("Sum of invalid IDs with 2 parts: %d" % total_2)
print("Sum of all invalid IDs: %d" % total_all)