# 2015 - Day 8 - Part 1
from queue import Empty
import re

fname = "day7.txt"
fp = open(fname, "r")

circuit_dict = {}

instruction_regex = re.compile(r"(.*) -> (.*)")
operation_regex = re.compile(
    r"(\w+) (AND|OR|NOT|LSHIFT|RSHIFT) (\w+)|(NOT) (\w+)")

circuit_list = [x.strip() for x in fp.readlines()]
print(circuit_list)
