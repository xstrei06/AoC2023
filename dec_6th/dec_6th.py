# day 6

import math

f = open("input.txt", "r")

data_in = f.readlines()

data_in = [x.strip().split() for x in data_in]
data_in[0].pop(0)
data_in[1].pop(0)

result_1 = 1
race = ''
time = ''
result_2 = 1

for i in range(len(data_in[0])):
    count = 0
    race += data_in[0][i]
    time += data_in[1][i]
    for j in range(math.ceil(int(data_in[0][i])/2)):
        if j * (int(data_in[0][i]) - j) > int(data_in[1][i]):
            count += 1
    count = count * 2 if int(data_in[0][i]) % 2 == 1 else count * 2 + 1
    result_1 *= count

count = 0
for j in range(math.ceil(int(race)/2)):
    if j * (int(race) - j) > int(time):
        count += 1
count = count * 2 if int(race) % 2 == 1 else count * 2 + 1
result_2 *= count

print("part one: " + str(result_1))
print("part two: " + str(result_2))
