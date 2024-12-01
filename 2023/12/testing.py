from aochelpers import read

f = read("../..").splitlines()
r = []
for i in f:
    a, b = i.split(" ")
    b = list(map(int, b.split(",")))
    r.append((a, b))

row, ins = r[-1]
row = [i for i in row.split('.') if i != ""]

print(row, ins)
# for row, ins in r:
#     print(row, ins)
