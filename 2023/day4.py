# Day 4 - Part 1
fp = open("day4.txt", "r")

cards_data = {
    "winning_numbers": [],
    "my_numbers": []
}

day4part1total = 0

for line in fp:
    number = "0"
    numbers_data = line.split(":")
    numbers_list = numbers_data[1].split("|")
    for char in numbers_list[0]:
        if char.isdigit():
            number = number+char
        elif char in " ":
            cards_data["winning_numbers"].append(int(number))
            number = "0"
    for char in numbers_list[1]:
        if char.isdigit():
            number = number+char
        elif char in " ":
            cards_data["my_numbers"].append(int(number))
            number = "0"
    cards_data["my_numbers"].append(int(number))

    count = -1

    for winning_number in cards_data["winning_numbers"]:
        for my_number in cards_data["my_numbers"]:
            if winning_number == my_number and winning_number > 0:
                count += 1

    if count > -1:
        day4part1total = 2**count+day4part1total

    cards_data["winning_numbers"].clear()
    cards_data["my_numbers"].clear()

print(f"Day4 Part 1 Total: {day4part1total}")

# Day 4 - Part 2
fp.seek(0)
day4part2total = 0
card_count_list = [1]*len(fp.readlines())
fp.seek(0)

for line in fp:
    number = "0"
    numbers_data = line.split(":")
    game_number = int(numbers_data[0].strip("Card "))
    numbers_list = numbers_data[1].split("|")

    for char in numbers_list[0]:
        if char.isdigit():
            number = number+char
        elif char in " ":
            cards_data["winning_numbers"].append(int(number))
            number = "0"

    for char in numbers_list[1]:
        if char.isdigit():
            number = number+char
        elif char in " ":
            cards_data["my_numbers"].append(int(number))
            number = "0"
    cards_data["my_numbers"].append(int(number))

    count = 0
    for list_count in range(0, card_count_list[game_number-1]):
        for winning_number in cards_data["winning_numbers"]:
            for my_number in cards_data["my_numbers"]:
                if winning_number == my_number and winning_number > 0:
                    count += 1
        if count > 0:
            for index in range(0, count):
                card_count_list[game_number+index] += 1

        cards_data["winning_numbers"].clear()
        cards_data["my_numbers"].clear()

for card_count in card_count_list:
    day4part2total = day4part2total+card_count

print(f"Day4 Part 2 Total: {day4part2total}")
fp.close()
