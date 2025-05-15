# 2015 - Day 4 - Part 1

import hashlib
import re

fname = "day4.txt"
fp = open(fname, "r")

secret = fp.readline()

day4part1total = 0

while True:
    md5hash = hashlib.md5(
        bytes(secret+str(day4part1total), "utf-8")).hexdigest()
    if re.search("^00000", md5hash):
        break
    day4part1total += 1

print(f"2015 - Day 4 Part 1 Total: {day4part1total}")

# 2015 - Day 4 - Part 2

day4part2total = 0

while True:
    md5hash = hashlib.md5(
        bytes(secret+str(day4part2total), "utf-8")).hexdigest()
    if re.search("^000000", md5hash):
        break
    day4part2total += 1

print(f"2015 - Day 4 Part 2 Total: {day4part2total}")

fp.close()
