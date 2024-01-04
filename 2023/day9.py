# Day 9 - Part 1

fp = open("day9.txt", "r")


def get_prediction(number_sequence: list):
    difference_list = []
    for index in range(len(number_sequence)-1):
        difference_list.append(
            number_sequence[index+1]-number_sequence[index])
    flag = 0
    for item in difference_list:
        if item != 0:
            flag = 1
    if flag == 0:
        return False, 0, difference_list
    return True, difference_list[-1], difference_list


day9part1total = 0
for line in fp:
    sequence = [int(num) for num in line.split()]
    differences_list = []
    intermediate_list = []
    end_flag, difference, intermediate_list = get_prediction(sequence)
    while end_flag:
        differences_list.append(difference)
        end_flag, difference, intermediate_list = get_prediction(
            intermediate_list)
    day9part1total += sum(differences_list)+sequence[-1]

print(f"Day 9 Part 1 Total: {day9part1total}")

# Day 9 - Part 2
fp.seek(0)
day9part2total = 0

for line in fp:
    sequence = [int(num) for num in line.split()]
    differences_list = []
    intermediate_list = []
    sequence.reverse()
    end_flag, difference, intermediate_list = get_prediction(sequence)
    while end_flag:
        differences_list.append(difference)
        end_flag, difference, intermediate_list = get_prediction(
            intermediate_list)
    day9part2total += sum(differences_list)+sequence[-1]

print(f"Day 9 Part 2 Total: {day9part2total}")

fp.close()
