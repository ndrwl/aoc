file = open("input.txt", "r")
lines = file.read().splitlines()

def parse_line(line):
    colon_index = line.index(':')
    separator_index = line.index('|')

    winning_numbers = {int(x) for x in line[colon_index+1:separator_index].strip().split(' ') if x.strip() != ''}
    candidate_numbers = [int(x) for x in line[separator_index+1:].strip().split(' ') if x.strip() != '']
    return winning_numbers, candidate_numbers

def count_winners(winning_numbers, candidate_numbers):
    count = 0
    for number in candidate_numbers:
        if number in winning_numbers:
            count += 1
    return count

original_prize = 0
card_count = [1] * (len(lines))

for idx in range(len(lines)):
    winning_numbers, candidate_numbers = parse_line(lines[idx])
    winners = count_winners(winning_numbers, candidate_numbers)
    original_prize += 1 << (winners - 1) if winners > 0 else 0

    for i in range(winners):
        card_count[idx + i + 1] += card_count[idx]

print("Original prize: %d" % original_prize)
print("Card count: %d" % sum(card_count))
