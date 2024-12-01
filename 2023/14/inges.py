from aochelpers import read

f = read("../..").splitlines()

r = []
t = 0
for y, v in enumerate(f):
    k = []
    for x, c in enumerate(v):
        if c == 'O':
            i = y - 1
            while i > -1:
                if i >= len(r) or r[i][x] == '#' or r[i][x] == 'O':
                    break
                i -= 1
            i += 1
            if i == y:
                k.append(c)
            else:
                r[i][x] = c
                k.append('.')
        else:
            k.append(c)
    r.append(k)

t = 0
for i, row in enumerate(r):
    t += row.count('O') * (len(r) - i)

print(t)
# print("".join(row))
