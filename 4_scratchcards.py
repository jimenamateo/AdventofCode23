## DAY 4
## Scratchcards

## PART 1

cards = []
with open('data/input4.txt') as file:
    for line in file:
        _, line = line.split(': ')
        left, right = line.split('|')
        left_numbers = set(map(int, left.split()))  
        right_numbers = set(map(int, right.split()))
        cards.append((left_numbers, right_numbers))

points = 0
for card in cards:
    winning, mine = card
    common = len(winning.intersection(mine))
    if common > 0:
        win = 2**(common-1)
    else:
        win = 0
    points += win
print(points)

## PART 2

ncards = {}
for card in range(len(cards)):
    ncards[card] = 1

for i in range(len(cards)):
    n = ncards[i]
    winning, mine = cards[i]
    common = len(winning.intersection(mine))
    for j in range(common):
        if i+j+1 in ncards:
            ncards[i+j+1] += n
print(ncards)

total = sum(ncards.values())
print(total)
