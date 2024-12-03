with open("input.txt", "r") as f:
    lines = f.read().splitlines()

counter = 0
for line in lines:
    range1 = list(map(int, line.split(",")[0].split("-")))
    range2 = list(map(int, line.split(",")[1].split("-")))
    values1 = [x for x in range(range1[0], range1[1] + 1)]
    values2 = [x for x in range(range2[0], range2[1] + 1)]

    if any(x in values2 for x in values1):
        counter += 1
    elif any(x in values1 for x in values2):
        counter += 1

print(counter)

# 861
