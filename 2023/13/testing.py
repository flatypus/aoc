from aochelpers import read

f = read("../..").split('\n\n')

r = []
for i in f:
    r.append(i.split('\n'))

t = 0


def run(i, last=-1):
    for start in range(1, len(i)):
        a, b = i[:start], i[start:][::-1]
        a, b = sorted([a, b], key=lambda x: len(x))
        b = b[len(b)-len(a):]
        if a == b and start * 100 != last:
            return start * 100

    c = []
    for j in range(len(i[0])):
        c.append(''.join([i[k][j] for k in range(len(i))]))

    # for p in c:
    #     print(''.join(p))
    # horizontal mirror
    for start in range(1, len(c)):
        a, b = c[:start], c[start:][::-1]
        a, b = sorted([a, b], key=lambda x: len(x))
        b = b[len(b)-len(a):]
        if a == b and start != last:
            return start


def createVariation(m):
    f = []
    for x, y in [[x, y] for x in range(len(m[0])) for y in range(len(m))]:
        copy = [list(i) for i in m].copy()
        copy[y][x] = '.' if copy[y][x] == '#' else '#'
        f.append(copy)
    return f


for i in r:
    p = run(i)
    for j in createVariation(i):
        result = run(j, p) # type: ignore
        print(result)
        if result != None and result != p:
            # for k in j:
            #     print(''.join(k))
            t += result
            break
    # break
print(t)
