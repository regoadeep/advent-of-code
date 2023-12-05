# Day 1 - Part 1
fp = open("day1.txt", "r")

firstnum = -1
lastnum = -1

day1part1total = 0

for line in fp:
    for char in line:
        if char.isdigit():
            if firstnum == -1:
                firstnum = int(char)*10
            if lastnum == -1:
                lastnum = int(char)
            else:
                lastnum = int(char)
    day1part1total = day1part1total+firstnum+lastnum
    firstnum = lastnum = -1

print(f'Day 1 Part 1 output: {day1part1total}')

# Day 1 - Part 2
fp.seek(0)

day1part2total = 0
lineindex = 0

for line in fp:
    while lineindex < len(line):
        if line[lineindex].isdigit():
            if firstnum == -1:
                firstnum = int(line[lineindex])*10
            lastnum = int(line[lineindex])
        elif line[lineindex] in "onetwhrfuivsxg":
            if line[lineindex:lineindex+3] == "one":
                if firstnum == -1:
                    firstnum = 10
                lastnum = 1
                lineindex += 1
            elif line[lineindex:lineindex+3] == "two":
                if firstnum == -1:
                    firstnum = 20
                lastnum = 2
                lineindex += 1
            elif line[lineindex:lineindex+5] == "three":
                if firstnum == -1:
                    firstnum = 30
                lastnum = 3
                lineindex += 3
            if line[lineindex:lineindex+4] == "four":
                if firstnum == -1:
                    firstnum = 40
                lastnum = 4
                lineindex += 2
            elif line[lineindex:lineindex+4] == "five":
                if firstnum == -1:
                    firstnum = 50
                lastnum = 5
                lineindex += 2
            elif line[lineindex:lineindex+3] == "six":
                if firstnum == -1:
                    firstnum = 60
                lastnum = 6
                lineindex += 1
            if line[lineindex:lineindex+5] == "seven":
                if firstnum == -1:
                    firstnum = 70
                lastnum = 7
                lineindex += 3
            elif line[lineindex:lineindex+5] == "eight":
                if firstnum == -1:
                    firstnum = 80
                lastnum = 8
                lineindex += 3
            elif line[lineindex:lineindex+4] == "nine":
                if firstnum == -1:
                    firstnum = 90
                lastnum = 9
                lineindex += 2
        lineindex += 1
    day1part2total = day1part2total+firstnum+lastnum
    firstnum = lastnum = -1
    lineindex = 0

print(f'Day 1 Part 1 output: {day1part2total}')
fp.close()
