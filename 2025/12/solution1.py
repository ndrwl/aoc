file = open("input.txt", "r")
lines = file.read().splitlines()

def parse_problem(line):
    parts = line.split(':')
    size_part = parts[0]
    counts_part = parts[1].strip()
    size_parts = size_part.split('x')
    width = int(size_parts[0])
    height = int(size_parts[1])
    counts = [int(x) for x in counts_part.split()]
    return width, height, counts

def area_fits(width, height, counts, patterns):
    total_area = width * height
    used_area = 0
    for i in range(len(counts)):
        used_area += counts[i] * patterns[i]
    return used_area <= total_area

patterns = []
problems = []

for line in lines:
    if line == '':
        continue
    if line.endswith(':'):
        patterns.append(0)
    elif ':' in line:
        problems.append(parse_problem(line))
    else:
        patterns[-1] += line.count('#')

fits = sum(1 for width, height, counts in problems if area_fits(width, height, counts, patterns))
print("Number of fitting problems: %d" % fits)