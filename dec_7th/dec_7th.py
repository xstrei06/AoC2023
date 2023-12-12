# day 7

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
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def compare(item1, item2):
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
    for char in hand:
        if char not in distinct:
            max_count[char] = 1
            distinct.add(char)
            distinct_count += 1
        else:
            max_count[char] += 1

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

print("five", five)
print("four", four)
print("full", full)
print("three", three)
print("two", two)
print("one", one)
print("high", high)

