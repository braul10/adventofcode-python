with open("input.txt", "r") as f:
    lines = f.readlines()

safes = 0

def check_line(line):
    line = line.strip()
    levels = list(map(int, line.split(" ")))
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    if len([x for x in diffs if abs(x) > 3]) > 0:
        return False

    zeros = len([x for x in diffs if x == 0])
    ups = len([x for x in diffs if x > 0])
    downs = len([x for x in diffs if x < 0])

    if zeros == 0 and (ups == 0 or downs == 0):
        return True
    
    return False

for line in lines:
    if check_line(line):
        safes += 1

print(safes)

# 411
