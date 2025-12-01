file = open("input.txt", "r")
lines = file.read().splitlines()

word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def try_get_number(line, idx):
    if (line[idx].isnumeric()):
        return True, int(line[idx])
    for number, word_number in enumerate(word_numbers):
        if (line[idx:idx + len(word_number)] == word_number):
            return True, number + 1
    return False, 0

numbers = []

for line in lines:
    found_first = False
    first_number = 0
    last_number = 0
    for idx, char in enumerate(line):
        found, num = try_get_number(line, idx)
        if (found):
            if (not found_first):
                found_first = True
                first_number = num
            last_number = num
    numbers.append(first_number * 10 + last_number)

print(sum(numbers))
