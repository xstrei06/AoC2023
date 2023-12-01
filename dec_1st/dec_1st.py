# day 1
import numpy as np
import re

f = open("input.txt", "r")
strings = [line for line in f]
f.close()

pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|zero))'
numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

part1 = strings.copy()
part2 = strings.copy()

for i in range(len(strings)):
    part1[i] = ''.join(c for c in part1[i] if c.isdigit())
    part1[i] = part1[i][0] + part1[i][-1]
    matches = re.findall(pattern, strings[i])
    print(strings[i], end='')
    if len(matches) == 1:
        part2[i] = part2[i].replace(matches[0], numbers[matches[0]] + matches[0])
    elif len(matches) >= 2:
        part2[i] = part2[i].replace(matches[0], numbers[matches[0]] + matches[0], 1)
        part2[i] = part2[i].replace(matches[-1], matches[-1] + numbers[matches[-1]])
    print(part2[i], end='')
    part2[i] = ''.join(c for c in part2[i] if c.isdigit())
    part2[i] = part2[i][0] + part2[i][-1]
    print(part2[i])

sum_vals1 = np.sum(part1, dtype=int)
sum_vals2 = np.sum(part2, dtype=int)

print('Part one: ' + str(sum_vals1))
print('Part two: ' + str(sum_vals2))
