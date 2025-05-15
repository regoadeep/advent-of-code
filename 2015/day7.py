# 2015 - Day 7 - Part 1
from queue import Empty
import re

fname = "day7.txt"
fp = open(fname, "r")


# def find_value(circuit_list, input_wire):
#     instruction_regex = re.compile(
#     r"(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)|(NOT) (\w+) -> (\w+)|(\w+) -> (\w+)")
#     value=0
#     for line in circuit_list:
#         if input_wire in line:

#     else:
#         find_value(circuit_list, input_wire)
#     return(value)


circuit_dict = {}
instruction_regex = re.compile(
    r"(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)|(NOT) (\w+) -> (\w+)|(\w+) -> (\w+)")
operation_regex = re.compile(r"AND|OR|LSHIFT|RSHIFT|NOT")

circuit_list = [x.strip() for x in fp.readlines()]
# find_value(circuit_list, "e")

for line in circuit_list:
    value = ""
    instruction_list = re.findall(instruction_regex, line)
    if "AND" in instruction_list[0][1]:
        if instruction_list[0][0].isnumeric() and instruction_list[0][2]:
            value = int(circuit_dict[instruction_list[0][0]]) & int(
                circuit_dict[instruction_list[0][2]])
            circuit_dict.update({instruction_list[0][3]: value})
        else:
            circuit_list.append(line)
    elif "OR" in instruction_list[0][1]:
        if instruction_list[0][0] in keys and instruction_list[0][2] in keys:
            value = int(circuit_dict[instruction_list[0][0]]) | int(
                circuit_dict[instruction_list[0][2]])
            circuit_dict.update({instruction_list[0][3]: value})
        else:
            circuit_list.append(line)
    elif "LSHIFT" in instruction_list[0][1]:
        if instruction_list[0][0] in keys:
            value = int(circuit_dict[instruction_list[0][0]]) << int(
                instruction_list[0][2])
            circuit_dict.update({instruction_list[0][3]: value})
        else:
            circuit_list.append(line)
    elif "RSHIFT" in instruction_list[0][1]:
        if instruction_list[0][0] in keys:
            value = int(circuit_dict[instruction_list[0][0]]) >> int(
                instruction_list[0][2])
            circuit_dict.update({instruction_list[0][3]: value})
        else:
            circuit_list.append(line)
    elif "NOT" in instruction_list[0][4]:
        if instruction_list[0][5] in keys:
            value = 65535-int(circuit_dict[instruction_list[0][5]])
            circuit_dict.update({instruction_list[0][6]: value})
        else:
            circuit_list.append(line)
    else:
        if instruction_list[0][7] in keys:
            value = int(circuit_dict[instruction_list[0][7]])
            circuit_dict.update({instruction_list[0][8]: value})
            if instruction_list[0][8] == "a":
                print(circuit_dict)
        elif instruction_list[0][7].isnumeric():
            value = int(instruction_list[0][7])
            circuit_dict.update({instruction_list[0][8]: value})
        else:
            circuit_list.append(line)

day7part1total = circuit_dict
print(circuit_dict)

# print(f'2015 - Day 7 Part 1 Total: {day7part1total}')
