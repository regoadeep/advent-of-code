# 2015 - Day 6 - Part 1
import re

fname = "day6.txt"
fp = open(fname, "r")

light_grid = [[0 for x in range(1000)] for x in range(1000)]
lights_sequence_regex = re.compile("[0-9]+")
day6part1total = 0

for line in fp.readlines():
    lights_list = [int(x) for x in re.findall(lights_sequence_regex, line)]
    if "turn on" in line:
        for row in range(lights_list[0], lights_list[2]+1):
            for column in range(lights_list[1], lights_list[3]+1):
                light_grid[row][column] = 1
    if "turn off" in line:
        for row in range(lights_list[0], lights_list[2]+1):
            for column in range(lights_list[1], lights_list[3]+1):
                light_grid[row][column] = 0
    if "toggle" in line:
        for row in range(lights_list[0], lights_list[2]+1):
            for column in range(lights_list[1], lights_list[3]+1):
                light_grid[row][column] = 0 if light_grid[row][column] == 1 else 1

for row in range(1000):
    for column in range(1000):
        if light_grid[row][column] == 1:
            day6part1total += 1

print(f"2015 - Day 6 Part 1 Total: {day6part1total}")

# 2015 - Day 6 - Part 2

fp.seek(0)
day6part2total = 0
light_grid = [[0 for x in range(1000)] for x in range(1000)]

for line in fp.readlines():
    lights_list = [int(x) for x in re.findall(lights_sequence_regex, line)]
    if "turn on" in line:
        for row in range(lights_list[0], lights_list[2]+1):
            for column in range(lights_list[1], lights_list[3]+1):
                light_grid[row][column] += 1
    if "turn off" in line:
        for row in range(lights_list[0], lights_list[2]+1):
            for column in range(lights_list[1], lights_list[3]+1):
                light_grid[row][column] = 0 if light_grid[row][column] == 0 else light_grid[row][column]-1
    if "toggle" in line:
        for row in range(lights_list[0], lights_list[2]+1):
            for column in range(lights_list[1], lights_list[3]+1):
                light_grid[row][column] += 2

for row in range(1000):
    for column in range(1000):
        day6part2total += light_grid[row][column]

print(f"2015 - Day 6 Part 2 Total: {day6part2total}")

fp.close()
