# day 7

from functools import cmp_to_key

f = open("input.txt", "r")

lines = f.readlines()

lines = [x.strip().split() for x in lines]

hands = {key: value for key, value in lines}
print(hands)

cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def compare(item1, item2, cards):
    i = 0
    while cards[item1[i]] == cards[item2[i]]:
        i += 1
    if cards[item1[i]] > cards[item2[i]]:
        return 1
    elif cards[item1[i]] < cards[item2[i]]:
        return -1
    else:
        return 0


five = []
four = []
full = []
three = []
two = []
one = []
high = []

for hand in hands.keys():
    distinct_count = 0
    distinct = set()
    max_count = {}
    J_count = 0
    for char in hand:
        if char == "J":
            J_count += 1
        if char not in distinct:
            max_count[char] = 1
            distinct.add(char)
            distinct_count += 1
        else:
            max_count[char] += 1
    if J_count == 0:
        if distinct_count == 1:
            five.append(hand)
        elif distinct_count == 2 and 4 in max_count.values():
            four.append(hand)
        elif distinct_count == 2 and 3 in max_count.values():
            full.append(hand)
        elif distinct_count == 3 and 3 in max_count.values():
            three.append(hand)
        elif distinct_count == 3 and 3 not in max_count.values():
            two.append(hand)
        elif distinct_count == 4:
            one.append(hand)
        else:
            high.append(hand)
    elif J_count == 1:
        if distinct_count == 2:
            five.append(hand)
        elif distinct_count == 3 and 2 in max_count.values():
            full.append(hand)
        elif distinct_count == 3 and 3 in max_count.values():
            four.append(hand)
        elif distinct_count == 4:
            three.append(hand)
        else:
            one.append(hand)
    elif J_count == 2:
        if distinct_count == 2:
            five.append(hand)
        elif distinct_count == 3:
            four.append(hand)
        elif distinct_count == 4:
            three.append(hand)
    elif J_count == 3:
        if distinct_count == 2:
            five.append(hand)
        elif distinct_count == 3:
            four.append(hand)
    elif J_count == 4:
        five.append(hand)
    elif J_count == 5:
        five.append(hand)

five = sorted(five, key=cmp_to_key(lambda x, y: compare(x, y, cards)))
four = sorted(four, key=cmp_to_key(lambda x, y: compare(x, y, cards)))
full = sorted(full, key=cmp_to_key(lambda x, y: compare(x, y, cards)))
three = sorted(three, key=cmp_to_key(lambda x, y: compare(x, y, cards)))
two = sorted(two, key=cmp_to_key(lambda x, y: compare(x, y, cards)))
one = sorted(one, key=cmp_to_key(lambda x, y: compare(x, y, cards)))
high = sorted(high, key=cmp_to_key(lambda x, y: compare(x, y, cards)))

rank = 1
winnings = 0
for item in [high, one, two, three, full, four, five]:
    for hand in item:
        print(hand)
        winnings += rank * int(hands[hand])
        rank += 1

print("part one: 252295678")
print("part two: ", winnings)
