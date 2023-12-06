from aochelpers import read, intify, bsearch
import re

file = read("../..").split('\n\n')
seeds, instructions = file[0], file[1:]

seeds = intify(re.findall(r'\d+', seeds))
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

maps = []

for i in instructions:
    i = i.split('\n')
    i = [intify(j.split()) for j in i if ":" not in j]
    i = sorted(i, key=lambda a: a[1])

    m = {}
    for new, start, length in i:
        m[start] = (new, length)

    maps.append(m)

print(maps)


n = float("inf")


print(seeds)
