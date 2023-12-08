from aochelpers import read, intify, bsearch
import re

file = read("../..").split('\n\n')
seeds, instructions = file[0], file[1:]

seeds = intify(re.findall(r'\d+', seeds))
seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

maps = []

for i in instructions:
    i = i.split('\n')
    i = [intify(j.split()) for j in i if ":" not in j]
    i = sorted(i, key=lambda a: a[1])

    m = {}
    for new, start, length in i:
        m[start] = (new, start + length)

    maps.append(m)


n = float("inf")

for seed_start, seed_end in seeds:
    print("Seed start:", seed_start, "Seed end:", seed_end)
    ranges = [(seed_start, seed_end)]
    for instruction_set in maps:
        print(ranges)
        new_ranges = []
        instructions = list(instruction_set.items())
        found = False
        for seed_start, seed_end in ranges:
            item = 0
            print("Seed start:", seed_start, "Seed end:", seed_end)
            while item < len(instructions):
                start, (new, end) = instructions[item]

        ranges = new_ranges.copy()
    if len(ranges) > 0 and min(ranges)[0] < n:
        n = min(ranges)[0]

print(n)
