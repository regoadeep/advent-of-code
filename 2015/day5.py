# 2015 - Day 5 - Part 1
import re

fname = "day5.txt"
fp = open(fname, "r")

vowels_regex = re.compile("[aeiou]")
bad_regex = re.compile("(ab|cd|pq|xy)")
double_regex = re.compile("(\\S)\\1+")

day5part1total = 0

for line in fp.readlines():
    vowels_flag = 0
    double_flag = 0
    vowels_string = re.findall(vowels_regex, line)
    string = ""
    if re.search(bad_regex, line):
        continue

    elif len(vowels_string) >= 3:
        vowels_flag = 1

    if re.search(double_regex, line):
        double_flag = 1

    if vowels_flag == 1 and double_flag == 1:
        day5part1total += 1

print(f"2015 - Day 5 Part 1 Total: {day5part1total}")

# 2015 - Day 5 - Part 2

pair_regex = re.compile("([a-z][a-z]).*\\1")
letter_regex = re.compile("([a-z])[a-z]\\1")

fp.seek(0)
day5part2total = 0

for line in fp.readlines():
    pair_flag = 0
    letter_flag = 0
    if re.search(pair_regex, line):
        pair_flag = 1
    if re.search(letter_regex, line):
        letter_flag = 1

    if pair_flag == 1 and letter_flag == 1:
        day5part2total += 1

print(f"2015 - Day 5 Part 2 Total: {day5part2total}")
