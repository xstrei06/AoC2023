# day 3

import re

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

pattern = r'\b\d+\b'

engine = 0

gears = 0

for i in range(len(lines)):
    numbers = set(re.findall(pattern, lines[i]))
    for num in numbers:
        indexes = [x.start() for x in re.finditer(r'\b' + re.escape(num) + r'\b', lines[i])]
        for idx in indexes:
            try:
                added = 0
                for j in range(idx, idx + len(num)):
                    if i-1 >= 0:
                        if lines[i-1][j] != '.' and not lines[i-1][j].isdigit():
                            engine += int(num)
                            raise IndexError
                    if i+1 < len(lines):
                        if lines[i+1][j] != '.' and not lines[i+1][j].isdigit():
                            engine += int(num)
                            raise IndexError
                if idx-1 >= 0:
                    if lines[i][idx-1] != '.' and not lines[i][idx-1].isdigit():
                        engine += int(num)
                        raise IndexError
                    if i-1 >= 0:
                        if lines[i-1][idx-1] != '.' and not lines[i-1][idx-1].isdigit():
                            engine += int(num)
                            raise IndexError
                    if i+1 < len(lines):
                        if lines[i+1][idx-1] != '.' and not lines[i+1][idx-1].isdigit():
                            engine += int(num)
                            raise IndexError
                if idx + len(num) < len(lines[i]):
                    if lines[i][idx + len(num)] != '.' and not lines[i][idx + len(num)].isdigit():
                        engine += int(num)
                        raise IndexError
                    if i-1 >= 0:
                        if lines[i-1][idx + len(num)] != '.' and not lines[i-1][idx + len(num)].isdigit():
                            engine += int(num)
                            raise IndexError
                    if i+1 < len(lines):
                        if lines[i+1][idx + len(num)] != '.' and not lines[i+1][idx + len(num)].isdigit():
                            engine += int(num)
                            raise IndexError
            except IndexError:
                pass

for i in range(len(lines)):
    stars = [x.start() for x in re.finditer(r'\*', lines[i])]
    for star in stars:
        numbers = []
        for j in range(i-1, i+2):
            if j < 0 or j >= len(lines):
                continue
            nums = set(re.findall(pattern, lines[j]))
            for num in nums:
                indexes = [x.start() for x in re.finditer(r'\b' + re.escape(num) + r'\b', lines[j])]
                print(str(num) + '=' + str(indexes))
                for idx in indexes:
                    if (idx + len(num) >= star >= idx) or (star-1 <= idx <= star+1):
                        numbers.append(num)
        print(numbers)
        if len(numbers) == 2:
            gears += int(numbers[0]) * int(numbers[1])

print('part one: ' + str(engine))
print('part two: ' + str(gears))
