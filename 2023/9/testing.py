from aochelpers import read

f = [list(map(int, i.split())) for i in read("../..").splitlines()]

f = f[::-1]

s = 0


for i in f:
    r = [i]
    while not all([i == 0 for i in r[-1]]):
        n = [r[-1][j+1] - r[-1][j] for j in range(len(r[-1])-1)]
        r.append(n)

    r = r[::-1]

    for i in range(len(r)):
        if i == 0:
            r[0] = [0, *r[0]]
        else:
            r[i] = [r[i][0]-r[i-1][0], *r[i]]
    print(r)
    s += r[-1][0]
    # break
print(s)
