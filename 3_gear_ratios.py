## DAY 3
## GEAR RATIOS

## PART 1

from point import Point

NEIGHBORS = [Point(-1, -1), Point(-1, 0), Point(-1, 1), 
             Point(0, -1),                Point(0, 1), 
             Point(1, -1),  Point(1, 0),  Point(1, 1)]

engine = []

with open('data/input3.txt') as file:
    for line in file:
        lines = []
        for char in line:
            if char != '\n':
                lines.append(char)
        engine.append(lines)

numsum = 0
for i in range(len(engine)):
    processed = set()
    for j in range(len(engine[i])):
        point = Point(i, j)
        if point in processed:
            continue
        
        num_points = []
        while point.y < len(engine[point.x]) and engine[point.x][point.y].isdigit():
            num_points.append(point)
            processed.add(point)
            point = Point(point.x, point.y + 1)
        if not num_points:
            continue
        number = 0
        is_part = False
        for point in num_points:
            number = number * 10 + int(engine[point.x][point.y])
            if not is_part:
                for neighbor in NEIGHBORS:
                    neighborpoint = point + neighbor
                    if neighborpoint.x >= 0 and neighborpoint.x < len(engine) and neighborpoint.y >= 0 and neighborpoint.y < len(engine[neighborpoint.x]):
                        neighborchar = engine[neighborpoint.x][neighborpoint.y]
                        if not (neighborchar.isdigit() or neighborchar == "."):
                            is_part = True
                            break
        if is_part:
            numsum += number
#           print(number, numsum)


## PART 2
          
gear = {}
for i in range(len(engine)):
    processed = set()
    for j in range(len(engine[i])):
        point = Point(i, j)
        if point in processed:
            continue
        
        num_points = []
        while point.y < len(engine[point.x]) and engine[point.x][point.y].isdigit():
            num_points.append(point)
            processed.add(point)
            point = Point(point.x, point.y + 1)
        if not num_points:
            continue
        number = 0
        star = set()
        for point in num_points:
            number = number * 10 + int(engine[point.x][point.y])
            for neighbor in NEIGHBORS:
                neighborpoint = point + neighbor
                if neighborpoint.x >= 0 and neighborpoint.x < len(engine) and neighborpoint.y >= 0 and neighborpoint.y < len(engine[neighborpoint.x]):
                    neighborchar = engine[neighborpoint.x][neighborpoint.y]
                    if neighborchar == "*":
                        star.add(neighborpoint)
        for neighborpoint in star:
            if neighborpoint not in gear:
                gear[neighborpoint] = []
            gear[neighborpoint].append(number)

gearratiotot = 0
for neighbor, numbers in gear.items():
    if len(numbers) == 2:
        gearratio = numbers[0]*numbers[1]
        gearratiotot += gearratio
        print(gearratio, gearratiotot)

