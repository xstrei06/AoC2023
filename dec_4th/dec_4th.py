# day 4

f = open("input.txt", "r")
lines = f.readlines()

lines = list(map(lambda line: line.strip(), lines))
lines = list(map(lambda line: line.split("|"), lines))
lines = list(map(lambda line: list(map(lambda x: x.split(":"), line)), lines))

winning = list(map(lambda line: line[0][1].split(), lines))
owned = list(map(lambda line: line[1][0].split(), lines))

cards = [1 for i in range(len(lines))]
cards_winning = [0 for j in range(len(lines))]

for i in range(len(winning)):
    numbers = 0
    for num in owned[i]:
        if num in winning[i]:
            numbers += 1
    cards_winning[i] = numbers
    if cards_winning[i] > 0:
        for j in range(i+1, i+1+cards_winning[i]):
            cards[j] += cards[i]

points = list(map(lambda x: (2**(x-1) if x > 0 else x), cards_winning))

print('part one: ' + str(sum(points)))
print('part two: ' + str(sum(cards)))
