from functools import cmp_to_key

file = open("input.txt", "r")
lines = file.read().splitlines()

hand_bids = [(x, int(y.strip())) for x, y in [line.split(" ") for line in lines]]

def hand_type(hand):
    hand_counts = {}
    for card in hand:
        if card not in hand_counts:
            hand_counts[card] = 0
        hand_counts[card] += 1
    counts = sorted(hand_counts.values(), reverse=True)
    if counts[0] == 5:
        return 6
    elif counts[0] == 4:
        return 5
    elif counts[0] == 3 and counts[1] == 2:
        return 4
    elif counts[0] == 3:
        return 3
    elif counts[0] == 2 and counts[1] == 2:
        return 2
    elif counts[0] == 2:
        return 1
    else:
        return 0

def card_value(card):
    return '23456789TJQKA'.index(card)

def compare_hand(hand1, hand2):
    if hand_type(hand1) > hand_type(hand2):
        return 1
    elif hand_type(hand1) < hand_type(hand2):
        return -1

    for idx in range(len(hand1)):
        if card_value(hand1[idx]) > card_value(hand2[idx]):
            return 1
        elif card_value(hand1[idx]) < card_value(hand2[idx]):
            return -1

    return 0

hand_bids = sorted(hand_bids, key=cmp_to_key(lambda hand_bid1, hand_bid2: compare_hand(hand_bid1[0], hand_bid2[0])))

prize = 0
for idx in range(len(hand_bids)):
    hand, bid = hand_bids[idx]
    prize += bid * (idx + 1)

print("Total prize: %d" % prize)