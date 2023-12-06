## DAY 4
## Scratchcards

## PART 1

lines = []
positions = []

with open('data/input5.txt') as file:
    for line in file:
        lines.append(line.strip())
    #print(lines)
for i in range(len(lines)):
    if 'map' in lines[i]:
        positions.append(i)
#print(positions)


seeds = lines[0].split(': ')[1]
seeds = [int(num) for num in seeds.split(' ')]
#print(seeds)

raw_maps = []
for i in range(len(positions)):
    start = positions[i]
    if i < len(positions)-1:
        end = positions[i+1] - 1
    else:
        end = len(lines)
    map = lines[start+1: end]
    raw_maps.append(map)
#print(raw_maps)

maps = []
for i in range(len(raw_maps)):
    map = raw_maps[i]
    map1 = []
    for ran in map:
        ran = [int(num) for num in ran.split(' ')]
        map1.append(ran)
    maps.append(map1)

locations = []
for seed in seeds:
    num = seed
    for map in maps:
        print(map)
        for rule in map:
            destination, origin, ran = rule
            if num > origin and num < (origin+ran +1):
                dif = num - origin
                num = destination + dif
                break
        print(num)
    locations.append(num)
#print(locations)

start = min(locations)
print(start)
