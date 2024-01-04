# Day 8 Part 1

fp = open("day8.txt", "r")
sequence = fp.readline().strip()

fp.readline()
node_dict = {}

for line in fp:
    node_values = line.split("=")
    key = node_values[0].strip()
    maps = node_values[1].split(",")
    left_value = maps[0].strip(" (")
    right_value = maps[1].strip(" )\n")
    node_dict.update({key: [left_value, right_value]})

scan_index = 0
node_key = "AAA"
day8part1total = 0

while True:
    if scan_index == len(sequence):
        scan_index = 0
    if node_key == "ZZZ":
        break
    if sequence[scan_index] == "L":
        node_key = node_dict[node_key][0]
    else:
        node_key = node_dict[node_key][1]
    scan_index += 1
    day8part1total += 1

print(f'Day 8 Part 1 Total: {day8part1total}')


# Day 8 Part 2

node_keys_list = []
day8part2total = 1

for node_key in node_dict.keys():
    if node_key[2] == "A":
        node_keys_list.append(node_key)

node_key_steps = []
for node_key in node_keys_list:
    steps = 0
    node_key_temp = node_key
    while True:
        if scan_index == len(sequence):
            scan_index = 0
        if node_key_temp[2] == "Z":
            # print(steps)
            node_key_steps.append(steps)
            break
        if sequence[scan_index] == "L":
            node_key_temp = node_dict[node_key_temp][0]
        else:
            node_key_temp = node_dict[node_key_temp][1]
        scan_index += 1
        steps += 1


def get_LCM(num1: int, num2: int) -> int:
    max_number = max(num1, num2)
    min_number = min(num1, num2)
    lcm = max_number
    while True:
        if lcm % min_number == 0:
            return lcm
        lcm += max_number


day8part2total = 1
for steps in node_key_steps:
    day8part2total = get_LCM(day8part2total, steps)

print(f'Day 8 Part 2 Total: {day8part2total}')
