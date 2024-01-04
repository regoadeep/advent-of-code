# 2015 - Day 3 - Part 1

def deliver_present(direction: str, row: int, column: int):
    if direction in "<":
        column -= 1
    elif direction in ">":
        column += 1
    elif direction in "^":
        row -= 1
    elif direction in "v":
        row += 1
    return row, column


fname = "day3.txt"
fp = open(fname, "r")

line = fp.readline()
larrow = line.count("<")
rarrow = line.count(">")
uparrow = line.count("^")
downarrow = line.count("v")

column_width = larrow+rarrow+1
row_width = uparrow+downarrow+1

house_grid = [["" for x in range(column_width)]
              for y in range(row_width)]

row = int(row_width/2)
column = int(column_width/2)

house_grid[row][column] = "#"

for char in line:
    row, column = deliver_present(char, row, column)
    house_grid[row][column] = "#"

day3part1total = 0

for row in range(row_width):
    for column in range(column_width):
        if house_grid[row][column] == "#":
            day3part1total += 1

print(f"2015 - Day 3 Part 1 Total: {day3part1total}")

# 2015 - Day 3 - Part 2

santa_row = santa_robot_row = int(row_width/2)
santa_column = santa_robot_column = int(column_width/2)

house_grid = [["" for x in range(column_width)]
              for y in range(row_width)]

house_grid[santa_row][santa_column] = "#"

for index in range(0, len(line), 2):
    santa_row, santa_column = deliver_present(
        line[index], santa_row, santa_column)
    house_grid[santa_row][santa_column] = "#"

    santa_robot_row, santa_robot_column = deliver_present(
        line[index+1], santa_robot_row, santa_robot_column)
    house_grid[santa_robot_row][santa_robot_column] = "#"

day3part2total = 0

for row in range(row_width):
    for column in range(column_width):
        if house_grid[row][column] == "#":
            day3part2total += 1

print(f"2015 - Day 3 Part 2 Total: {day3part2total}")
