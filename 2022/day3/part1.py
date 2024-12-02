with open("input.txt", "r") as f:
    lines = f.readlines()

lines = list(map(str.strip, lines))

data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def get_priority(c):
    offset = 0
    if c.isupper():
        offset = 26
    return data[c.lower()] + offset


priorities_sum = 0
for line in lines:
    first_rucksack = line[: len(line) // 2]
    second_rucksack = line[len(line) // 2 :]
    for c in first_rucksack:
        if c in second_rucksack:
            priorities_sum += get_priority(c)
            break

print(priorities_sum)

# 7878
