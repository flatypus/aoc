from aochelpers import read
d = 1  # 0 for Part 1, or 1 for Part 2
n = 0
for s in read("../..").split("\n\n"):
    g = {(x, y): c
         for y, r in enumerate(s.splitlines())
         for x, c in enumerate(r)}
    w = max(x for x, y in g) + 1
    h = max(y for x, y in g) + 1
    for m in range(1, w):
        if sum(g[(l, y)] != g.get((m - l + m - 1, y), g[(l, y)])
                for l in range(m)
                for y in range(h)) == d:
            print(m)
            n += m
    for m in range(1, h):
        if sum(g[(x, t)] != g.get((x, m - t + m - 1), g[(x, t)])
                for x in range(w)
                for t in range(m)) == d:
            print(100 * m)
            n += 100 * m
    break
print(n)
