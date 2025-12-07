file = open("input.txt", "r")
lines = file.read().splitlines()

numbers = [[int(x.strip()) for x in line.strip().split(" ") if x.strip() != ''] for line in lines[:-1]]
symbols = [x.strip() for x in lines[-1].strip().split(" ") if x.strip() != '']

total = 0

for i in range(len(symbols)):
    symbol = symbols[i]
    if symbol == "*":
        sub_total = 1
        for row in range(len(numbers)):
            sub_total *= numbers[row][i]
        total += sub_total
    elif symbol == "+":
        sub_total = 0
        for row in range(len(numbers)):
            sub_total += numbers[row][i]
        total += sub_total

print("Total result: %d" % total)