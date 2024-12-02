with open("input.txt", "r") as f:
    lines = f.readlines()

safes = 0


def remove_first_bad_level_if_exists(line, offset):
    line = line.strip()
    levels = list(map(int, line.split(" ")))
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    zeros = len([x for x in diffs if x == 0])
    ups = len([x for x in diffs if x > 0])
    downs = len([x for x in diffs if x < 0])

    if zeros > 0:
        levels.pop(diffs.index(0) + 1)
        return levels

    if ups > 0 and downs > 0 and (ups == 1 or downs == 1):
        if ups <= downs:
            levels.pop(diffs.index([x for x in diffs if x > 0][0]) + offset)
            return levels
        else:
            levels.pop(diffs.index([x for x in diffs if x < 0][0]) + offset)
            return levels

    if len([x for x in diffs if abs(x) > 3]) > 0:
        levels.pop(diffs.index([x for x in diffs if abs(x) > 3][0]) + offset)
        return levels

    return levels


def check_line(levels):
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
    levels = remove_first_bad_level_if_exists(line, 0)
    if check_line(levels):
        safes += 1
    else:
        levels = remove_first_bad_level_if_exists(line, 1)
        if check_line(levels):
            safes += 1

print(safes)

# 465
