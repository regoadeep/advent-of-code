import re

# Day 15 - Part 1


def hash_function(string: str) -> int:
    hash_value = 0
    for char in string:
        hash_value = ((hash_value+ord(char))*17) % 256
    return hash_value


fp = open("day15.txt", "r")
init_sequence = fp.readline().split(",")
fp.close()

day15part1total = 0

for string in init_sequence:
    day15part1total = day15part1total+hash_function(string)

print(f"Day 15 Part 1 Total: {day15part1total}")

# Day 15 - Part 2

box_list = [""]*256
day15part2total = 0

for string in init_sequence:
    box_dict = {}
    label_details = re.split(r"(=|-)", string)
    box_number = hash_function(label_details[0])
    if (label_details[1] == "-"):
        if box_list[box_number] != "":
            box_dict = box_list[box_number]
            box_dict.pop(label_details[0], None)
        if len(box_dict) == 0:
            box_dict = ""
        box_list[box_number] = box_dict
    else:
        if box_list[box_number] != "":
            box_dict = box_list[box_number]
        box_dict[label_details[0]] = label_details[2]
        box_list[box_number] = box_dict

for box_number, box_dict in enumerate(box_list):
    box_total = 0
    if box_list[box_number] != "":
        for lens_index, label in enumerate(box_dict.items()):
            box_total += (box_number+1)*(lens_index+1)*int(label[1])
    day15part2total += box_total

print(f"Day 15 Part 2 Total: {day15part2total}")
