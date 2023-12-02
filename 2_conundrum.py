## DAY 2
## CUBE CONUNDRUM


## PART 1
games = []
with open('data/input2.txt') as file:
    for gamei in file:
        game = []
        gamei = gamei.split(': ')[-1]
        for setgame in gamei.split('; '):
            red, green, blue = 0, 0, 0
            for color in setgame.split(', '):
                color = color.strip().split(' ')
                if color[1] == "red":
                    red = int(color[0])
                elif color[1] == "green":
                    green = int(color[0])
                elif color[1] == "blue":
                    blue = int(color[0])
                else:
                    print("ERROR")
            game.append([red, green, blue])
        games.append(game)
    print(games)

maxred = 12
maxgreen = 13
maxblue = 14

validid = 0
for i in range(len(games)):
    gameid = i + 1
    valid = True
    for setgame in games[i]:
        red, green, blue = setgame
        if red > maxred or green > maxgreen or blue > maxblue:
            valid = False
            break
    if valid:
        validid += gameid
print(validid)

## PART 2

gameslist = []
for i in range(len(games)):
    maxred, maxgreen, maxblue = 0, 0, 0
    for setgame in games[i]:
        red, green, blue = setgame
        if red > maxred:
            maxred = red
        if green > maxgreen:
            maxgreen = green
        if blue > maxblue:
            maxblue = blue
    gameslist.append([maxred, maxgreen, maxblue])
print(gameslist)

gamesproduct = []
for game in gameslist:
    red, green, blue = game
    product = red*green*blue
    gamesproduct.append(product)
print(gamesproduct)

sumproduct = sum(gamesproduct)
print(sumproduct)