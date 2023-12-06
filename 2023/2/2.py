from collections import defaultdict
import re

with open("input.txt") as f:
    f = f.read().splitlines()


m = []
for i in f:
    i = i.split(":")[1]
    i = i.split(";")
    c = []
    for j in i:
        j = j.split(",")
        d = defaultdict(int)
        for k in j:
            k = k.strip()
            k = k.split()
            a, b = k
            a = int(a)
            d[b[0]] += a
        c.append(d)

    r = defaultdict(int)

    # min for each key
    for j in c:
        for k in j:
            r[k] = max(r[k], j[k])

    m.append(r)

n = 0
for g in m:
    print(g)
    r, g, b = g["r"], g["g"], g["b"]
    n += r * g * b
print(n)
