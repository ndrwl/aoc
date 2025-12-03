file = open("input.txt", "r")
lines = file.read().splitlines()

def calculate_joltate(bank, digits):
    min_index = 0
    joltage = 0
    for digit in range(1, digits + 1):
        digits_left = digits - digit
        pool = bank[min_index:-digits_left] if digits_left > 0 else bank[min_index:]
        next_digit = max(pool)
        min_index = bank.index(next_digit, min_index) + 1

        joltage = joltage * 10 + next_digit
    return joltage

total_joltage_2 = 0
total_joltage_12 = 0

for line in lines:
    bank = [int(x) for x in line]
    total_joltage_2 += calculate_joltate(bank, 2)
    total_joltage_12 += calculate_joltate(bank, 12)

print("Total joltage with 2 banks: %d" % total_joltage_2)
print("Total joltage with 12 banks: %d" % total_joltage_12)
