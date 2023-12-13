# Day 6 - Part 1
fp = open("day6.txt", "r")

line = fp.readline()
time_list = line.split()

line = fp.readline()
distance_list = line.split()

day6part1total = 1
for list_index in range(1, len(time_list)):
    count = 0
    time = int(time_list[list_index])
    for index in range(1, time):
        if (time-index)*index > int(distance_list[list_index]):
            count += 1
    day6part1total = day6part1total*count

print(day6part1total)
fp.close()

# Day 6 - Part 2
day6part2total = 0
time_list.remove("Time:")
distance_list.remove("Distance:")

time = int("".join(time_list))
distance = int("".join(distance_list))

for index in range(1, time):
    if (time-index)*index > distance:
        day6part2total += 1

print(day6part2total)
