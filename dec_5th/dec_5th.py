# day 5

f = open("input.txt", "r")
lines = f.readlines()
seeds = lines[0][7:].split()
seeds = list(map(int, seeds))
seeds2 = seeds.copy()
f.close()

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


def do_mapping(seed, mapping) -> int:
    map_list = list(filter(lambda arr: arr[1] <= seed <= arr[1]+arr[2]-1, mapping))
    return seed - map_list[0][1] + map_list[0][0] if map_list else seed


i = 0

while i < len(lines):
    if lines[i].startswith('seed-to-soil'):
        i += 1
        while lines[i] != '\n':
            seed_to_soil.append(lines[i].strip().split())
            i += 1
        seed_to_soil = list(map(lambda array: list(map(int, array)), seed_to_soil))
    elif lines[i].startswith('soil-to-fertilizer'):
        i += 1
        while lines[i] != '\n':
            soil_to_fertilizer.append(lines[i].strip().split())
            i += 1
        soil_to_fertilizer = list(map(lambda array: list(map(int, array)), soil_to_fertilizer))
    elif lines[i].startswith('fertilizer-to-water'):
        i += 1
        while lines[i] != '\n':
            fertilizer_to_water.append(lines[i].strip().split())
            i += 1
        fertilizer_to_water = list(map(lambda array: list(map(int, array)), fertilizer_to_water))
    elif lines[i].startswith('water-to-light'):
        i += 1
        while lines[i] != '\n':
            water_to_light.append(lines[i].strip().split())
            i += 1
        water_to_light = list(map(lambda array: list(map(int, array)), water_to_light))
    elif lines[i].startswith('light-to-temperature'):
        i += 1
        while lines[i] != '\n':
            light_to_temperature.append(lines[i].strip().split())
            i += 1
        light_to_temperature = list(map(lambda array: list(map(int, array)), light_to_temperature))
    elif lines[i].startswith('temperature-to-humidity'):
        i += 1
        while lines[i] != '\n':
            temperature_to_humidity.append(lines[i].strip().split())
            i += 1
        temperature_to_humidity = list(map(lambda array: list(map(int, array)), temperature_to_humidity))
    elif lines[i].startswith('humidity-to-location'):
        i += 1
        while i < len(lines):
            humidity_to_location.append(lines[i].strip().split())
            i += 1
        humidity_to_location = list(map(lambda array: list(map(int, array)), humidity_to_location))
    else:
        i += 1

# part one
for i in range(len(seeds)):
    seeds[i] = do_mapping(seeds[i], seed_to_soil)
    seeds[i] = do_mapping(seeds[i], soil_to_fertilizer)
    seeds[i] = do_mapping(seeds[i], fertilizer_to_water)
    seeds[i] = do_mapping(seeds[i], water_to_light)
    seeds[i] = do_mapping(seeds[i], light_to_temperature)
    seeds[i] = do_mapping(seeds[i], temperature_to_humidity)
    seeds[i] = do_mapping(seeds[i], humidity_to_location)

# part two
idxs = list(filter(lambda s: s % 2 == 0, range(len(seeds2))))
min_vals = [0 for i in idxs]
idx = 0

for i in idxs:
    map_list = []
    # first I did this, I found out which seed range to try, then I tried it, took about 4-5 hours
    # don't try this at home xD
    # rng = list(filter(lambda s: s % 10000 == 0, range(seeds2[i], seeds2[i]+seeds2[i+1])))
    rng = range(seeds2[i], seeds2[i]+seeds2[i+1])
    for j in rng:
        s = do_mapping(j, seed_to_soil)
        s = do_mapping(s, soil_to_fertilizer)
        s = do_mapping(s, fertilizer_to_water)
        s = do_mapping(s, water_to_light)
        s = do_mapping(s, light_to_temperature)
        s = do_mapping(s, temperature_to_humidity)
        s = do_mapping(s, humidity_to_location)
        if s < min_vals[idx] or min_vals[idx] == 0:
            min_vals[idx] = s
    idx += 1

print('part one: ' + str(min(seeds)))
print('part two: ' + str(min(min_vals)))
