from aochelpers import read

def is_valid_sequence(line):
    diff = line[1] - line[0]
    if not (1 <= abs(diff) <= 3):
        return False
    direction = diff / abs(diff)
    for i in range(1, len(line)):
        diff = line[i] - line[i-1]
        if not (1 <= abs(diff) <= 3) or diff / abs(diff) != direction:
            return False
    return True

count = 0
for line in read("../..").split('\n'):
    line = list(map(int, line.split()))
    if is_valid_sequence(line):
        count += 1

print(count)
