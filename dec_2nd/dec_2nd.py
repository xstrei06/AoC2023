# day 2
f = open("input.txt", "r")

lines = f.readlines()

split_games = list(map(lambda x: x.split(':'), lines))
games = [split_games[i][0].replace('Game ', '') for i in range(len(split_games))]
split_sets = [split_games[i][1].split(';') for i in range(len(split_games))]
sets = list(map(lambda x: list(map(lambda y: y.split(','), x)), split_sets))

colors_max = {'red': 0, 'green': 0, 'blue': 0}

max_values = [colors_max.copy() for _ in range(len(games))]
sum_games = 0
sum_powers = 0
for i in range(len(games)):
    for j in range(len(sets[i])):
        for item in sets[i][j]:
            value, color = item.split()
            if int(value) > max_values[i][color]:
                max_values[i][color] = int(value)
    if max_values[i]['red'] <= 12 and max_values[i]['green'] <= 13 and max_values[i]['blue'] <= 14:
        sum_games += int(games[i])
    sum_powers += max_values[i]['red'] * max_values[i]['green'] * max_values[i]['blue']

print('part one: ' + str(sum_games))
print('part two: ' + str(sum_powers))
