from collections import defaultdict

f = open("input.txt", 'r')

f = f.readlines()

t, d = f
t = t.split(":")[1].split()
d = d.split(":")[1].split()
n = []
for i in range(len(t)):
    n.append((int(t[i]), int(d[i])))

s = []

for x, y in n:
    a = 0
    for j in range(x + 1):
        if j * (x - j) > y:
            # print(j)
            a += 1
    # print(a)
    s.append(a)
    # print("\n")

r = 1
for i in s:
    r *= i
print(r)
