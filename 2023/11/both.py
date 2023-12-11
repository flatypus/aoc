from aochelpers import read

grid = read("../..").splitlines()

h_list = [i for i in range(len(grid[0])) if all(j[i] == "." for j in grid)]
v_list = [i for i, v in enumerate(grid) if all(j == "." for j in v)]

galaxies = [(x, y) for x in range(len(grid[0]))
            for y in range(len(grid)) if grid[y][x] == "#"]


def count(start, end, l, x):
    start, end = sorted([start, end])
    k = 0
    for i in l:
        if start <= i <= end:
            k += 1
        if i > end:
            break
    return (x - 1) * k + end - start


def main(x):
    score = 0
    for i in range(len(galaxies)):
        x1, y1 = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            x2, y2 = galaxies[j]
            score += count(x1, x2, h_list, x) + count(y1, y2, v_list, x)
    return score


print(main(2), main(1000000))
