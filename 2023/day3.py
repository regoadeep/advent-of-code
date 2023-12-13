# Day 3 - Part 1

def check_symbol(engine_schema: list, row_number: int, column_number: int, total_rows: int, total_columns: int) -> bool:
    if row_number+2 > rows:
        row_end = rows
    else:
        row_end = row_number+2

    if column_number+2 > columns:
        colum_end = columns
    else:
        colum_end = column_number+2

    valid_symbols = "@#$%&*-+=/"
    for i in range(row_number-1, row_end):
        for j in range(column_number-1, colum_end):
            char = engine_schema[i][j]
            if i >= 0 and j >= 0:
                if (char in valid_symbols):
                    return True
    return False


fp = open("day3.txt", "r")

columns = len(fp.readline())-1
fp.seek(0)
rows = len(fp.readlines())
fp.seek(0)


engine_schematic = [["." for x in range(columns)] for x in range(rows)]

day3part1total = 0
row_index = 0

for line in fp:
    column_index = 0
    for char in line:
        if char not in "\n":
            engine_schematic[row_index][column_index] = line[column_index]
            column_index += 1
    row_index += 1

for row_index in range(rows):
    flag = 0
    number = ""
    for column_index in range(columns):
        char = engine_schematic[row_index][column_index]
        if char.isdigit():
            number = number+char
            if check_symbol(engine_schematic, row_index, column_index, rows, columns) and flag == 0:
                flag = 1
        if not (char.isdigit()) and flag != 0:
            day3part1total += int(number)
            print(number)
            flag = 0
            number = ""
        elif not (char.isdigit()) and flag == 0:
            number = ""
    if flag != 0:
        day3part1total += int(number)
        print(number)
        flag = 0
        number = ""

print(f"Day 3 part 1 total: {day3part1total}")

# Day 3 - Part 2
