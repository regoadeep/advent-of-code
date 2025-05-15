# 2015 - Day 1 - Part 1

fname = "day1.txt"
day1part1total = 0
fp = open(fname, "r")
instructions = fp.readline()
fp.close()
for char in instructions:
    if char == "(":
        day1part1total += 1
    else:
        day1part1total -= 1

print(f"2015 - Day 1 Part 1 Total: {day1part1total}")

# 2015 - Day 1 - Part 2

day1part2total = 1
level = 0
for char in instructions:
    if char == "(":
        level += 1
    else:
        level -= 1
    if level == -1:
        break
    day1part2total += 1

print(f"2015 - Day 1 Part 2 Total: {day1part2total}")

fp.close()
