from aochelpers import read
import re

d=read("../..")
def sum(line):
    pairs = re.findall(r"mul\((\d+),(\d+)\)", line)
    count = 0
    for a, b in pairs:
        count += int(a) * int(b)
    return count

part_1 = sum(d)

part_2 = 0
for do_lines in d.split("do()"):
    valid = do_lines.split("don't()")[0]
    part_2 += sum(valid)
    
print(part_1, part_2)