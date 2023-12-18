# day 8

import math

file = open("input.txt", "r")

lines = file.readlines()

lines = [line.strip() for line in lines]

instructions = lines.pop(0)
lines.pop(0)

lines = [line.replace("=", '').replace("(", '')
         .replace(")", '').replace(",", '').split(" ") for line in lines]

network = {}

for line in lines:
    network[line[0]] = line[2:]

current = 'AAA'
steps_me = 0

ghost_current = [key for key in network.keys() if key.endswith('A')]

ghost_steps = [0 for i in range(len(ghost_current))]

while True:
    for instruction in instructions:
        if instruction == 'L':
            current = network[current][0]
        elif instruction == 'R':
            current = network[current][1]
        steps_me += 1
        if current == 'ZZZ':
            break

    if current == 'ZZZ':
        break

for i in range(len(ghost_current)):
    print(ghost_current[i])
    while True:
        for instruction in instructions:
            if instruction == 'L':
                ghost_current[i] = network[ghost_current[i]][0]
            elif instruction == 'R':
                ghost_current[i] = network[ghost_current[i]][1]
            ghost_steps[i] += 1
            if ghost_current[i].endswith('Z'):
                break
        if ghost_current[i].endswith('Z'):
            break

print('part one:', steps_me)
print('part two:', math.lcm(*ghost_steps))
