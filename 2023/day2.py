# Day 2 - Part 1
fp = open("day2.txt", "r")

games_list = []
number = ""
word = ""

red_cubes = 12
green_cubes = 13
blue_cubes = 14

day2part1total = 0

for line in fp:
    game_cubes = {
        "red": [],
        "green": [],
        "blue": []
    }
    values = line.split(":")
    for char in values[1]:
        if char.isdigit():
            number = number+char
        elif char in "bluegrnd":
            word = word+char
        elif char in ",;":
            game_cubes[word].append(int(number))
            word = ""
            number = ""
    game_cubes[word].append(int(number))
    word = ""
    number = ""
    games_list.append(game_cubes)

for game_number, cube_data in enumerate(games_list):
    flag = 0
    for count in cube_data["red"]:
        if count > red_cubes:
            flag = 1
    for count in cube_data["green"]:
        if count > green_cubes:
            flag = 1
    for count in cube_data["blue"]:
        if count > blue_cubes:
            flag = 1
    if flag == 0:
        day2part1total = day2part1total+game_number+1

print(f"Day2 Part1 Total: {day2part1total}")
fp.close()
day2part2total = 0

# Day 2 - Part 2

for cube_data in games_list:
    cube_data["red"].sort(reverse=True)
    cube_data["green"].sort(reverse=True)
    cube_data["blue"].sort(reverse=True)
    day2part2total = day2part2total + \
        (cube_data["red"][0]*cube_data["green"][0]*cube_data["blue"][0])

print(f"Day2 Part2 Total: {day2part2total}")
