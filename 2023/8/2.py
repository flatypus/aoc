from aochelpers import read
from collections import defaultdict
import re

f = read("../..").split('\n\n')
instructions, graph = f

instructions = [1 if i == 'R' else 0 for i in instructions]
graph = graph.strip().split('\n')

g = defaultdict(list)

for line in graph:
    start, p = line.split(" = ")
    out = re.findall(r"[A-Z0-9]{3}", p)
    g[start] += out

n = set()
for k, v in g.items():
    if k[-1] == 'A':
        n.add(k)


i = 0
c = 0
l = len(instructions)
cycle = []

for item in n:
    r = None
    p = None
    while True:
        if i >= l:
            i = 0

        if item[-1] == 'Z':
            if r is None:
                r = c
            else:
                p = c
                break
            c = 0

        item = g[item][instructions[i]]

        c += 1
        i += 1
    cycle.append(c)


# find LCM of cycle

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


ans = cycle[0]
for i in cycle[1:]:
    ans = lcm(ans, i)

print(ans)
