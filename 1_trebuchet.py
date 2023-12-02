## DAY 1
## TREBUCHET

## PART 1

with open('data/input1.txt') as file:
    sum = 0
    for line in file:
        first = None
        last = None
        for char in line:
            if char.isdigit():
                last = int(char)
                if first is None:
                    first = int(char)*10
        num = first+last
        sum += num
    print(sum)

## PART 2
letters = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
           "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open('data/input1.txt') as file2:
    sum = 0
    for line in file2:
        first = None
        last = None
        for i in range(len(line)):
            n = None
            if line[i].isdigit():
                n = int(line[i])
            else:
                for letter, num in letters.items():
                    if line[i:].startswith(letter):
                        n = num
            if n is not None:
                last = n
                if first is None:
                    first = int(n)*10
        num = first+last
        sum += num
    print(sum)
