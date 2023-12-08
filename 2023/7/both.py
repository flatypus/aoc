from aochelpers import read
from collections import Counter

f = read("../..").strip().split('\n')

p1 = []
p2 = []

m1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
m2 = ['J', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

for i in f:
    i = i.split()
    p1.append(([m1.index(j) for j in i[0]], int(i[1])))
    p2.append(([m2.index(j) for j in i[0]], int(i[1])))


def get_type(hand):
    counts = Counter(hand)
    values = counts.values()
    if len(counts) == 1:
        return 6
    if len(counts) == 2:
        if 4 in values:
            return 5
        if 3 in values and 2 in values:
            return 4
    if len(counts) == 3:
        if 3 in values and list(values).count(1) == 2:
            return 3
        if list(values).count(2) == 2:
            return 2
    if len(counts) == 4:
        return 1
    return 0


def get_max_type(hand):
    if 0 in hand:
        not_zero = [i for i in hand if i != 0]
        variations = [not_zero + [i] * hand.count(0) for i in range(1, 14)]
        return max([get_type(i) for i in variations])
    return get_type(hand)


def score(l, key_f):
    l = sorted(l, key=lambda x: (key_f(x[0]), x[0]))
    s = sum([(i + 1) * v[1] for i, v in enumerate(l)])
    return s


print(score(p1, get_type))
print(score(p2, get_max_type))
