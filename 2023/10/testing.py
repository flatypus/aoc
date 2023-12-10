from aochelpers import read

f = read("../..").splitlines()
f = [list(line) for line in f]


# find "S"
x, y = 0, 0
for i, line in enumerate(f):
    if "S" in line:
        x, y = line.index("S"), i
        break

positions = [[x, y]]


def next(x, y):
    if y - 1 >= 0 and f[y - 1][x] in ["|", "7", "F"]:
        if (f[y][x] == "S" or f[y][x] in ["|", "L", "J"]) and [x, y - 1] not in positions:
            return [x, y - 1]
    if y + 1 < len(f) and f[y + 1][x] in ["|", "J", "L"]:
        if (f[y][x] == "S" or f[y][x] in ["|", "7", "F"]) and [x, y + 1] not in positions:
            return [x, y + 1]
    if x - 1 >= 0 and f[y][x - 1] in ["-", "F", "L"]:
        if (f[y][x] == "S" or f[y][x] in ["-", "7", "J"]) and [x - 1, y] not in positions:
            return [x - 1, y]
    if x + 1 < len(f[y]) and f[y][x + 1] in ["-", "7", "J"]:
        if (f[y][x] == "S" or f[y][x] in ["-", "F", "L"]) and [x + 1, y] not in positions:
            return [x + 1, y]
    return [x, y]


def move(x, y, nx, ny):
    key = f[ny][nx]
    if key == "7":
        if x < nx:
            return "R"


nx, ny = next(x, y)
positions.append([nx, ny])
x, y = nx, ny
while f[y][x] != "S":
    nx, ny = next(x, y)
    if x == nx and y == ny:
        break
    positions.append([nx, ny])
    x, y = nx, ny

# print(positions)

max_x, max_y = len(f[0]), len(f)

out = set()


def _fill(x, y):
    # print(x, y)
    print(len(out))
    fill = set()
    if [x, y] not in positions and (x, y) not in out:
        out.add((x, y))
        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            return
        fill.add((x+1, y))
        fill.add((x-1, y))
        fill.add((x, y+1))
        fill.add((x, y-1))
        fill.add((x+1, y+1))
        fill.add((x-1, y-1))
        fill.add((x+1, y-1))
        fill.add((x-1, y+1))
        return fill


def floodfill(x, y):
    fill = _fill(x, y)
    if fill is None:
        return
    while len(fill) > 0:
        nx, ny = fill.pop()
        f = _fill(nx, ny)
        if f is not None:
            for i in f:
                fill.add(i)


_map = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
_map = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}

n_map = {}


for i, pos in enumerate(positions):
    if i == 0:
        continue
    x, y = pos
    if (x, y) in n_map:
        nx, ny = n_map[(x, y)]
    else:
        lx, ly = positions[i - 1]
        dx, dy = x - lx, y - ly
        nx, ny = _map[(dx, dy)]

    if [nx + x, ny + y] not in positions:
        floodfill(x + nx, y + ny)
        out.add((x + nx, y + ny))
        positions.append([x + nx, y + ny])
        n_map[(x + nx, y + ny)] = (nx, ny)


c = 0
for i in range(max_y):
    for j in range(max_x):
        if (j, i) in out:
            print(f"\033[91m{f[i][j]}\033[0m", end="")
        else:
            # green
            if [j, i] in positions:
                print(f"\033[92m{f[i][j]}\033[0m", end="")
            if [j, i] not in positions:
                print(f[i][j], end="")
                c += 1
    print()
