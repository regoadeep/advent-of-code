# 2015 - Day 2 - Part 1

fname = "day2.txt"
day1part1total = 0
fp = open(fname, "r")

for line in fp.readlines():
    dimensions = [int(number) for number in line.split("x")]
    area = (2*dimensions[0]*dimensions[1])+(2*dimensions[1]
                                            * dimensions[2])+(2*dimensions[0]*dimensions[2])
    day1part1total += area+min(dimensions[0]*dimensions[1], dimensions[1]
                               * dimensions[2], dimensions[0]*dimensions[2])

print(f"2015 - Day 2 Part 1 Total: {day1part1total}")

fp.seek(0)

day1part2total = 0
for line in fp.readlines():
    dimensions = [int(number) for number in line.split("x")]
    area = dimensions[0] * dimensions[1] * dimensions[2]
    dimensions.sort()
    day1part2total += area + (2*dimensions[0]) + (2*dimensions[1])

print(f"2015 - Day 2 Part 2 Total: {day1part2total}")

fp.close()
