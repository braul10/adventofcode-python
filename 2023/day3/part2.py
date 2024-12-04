with open("input.txt", "r") as f:
    lines = f.read().splitlines()

matrix = [list(line) for line in lines]


def get_surroundings(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])
    surroundings = []
    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            surroundings.append((matrix[nr][nc], (nr, nc)))
    return surroundings


numbers_with_gears = []
for row_idx, row in enumerate(matrix):
    col_idx = 0
    while col_idx < len(row):
        if row[col_idx].isdigit():
            start = col_idx
            while col_idx < len(row) and row[col_idx].isdigit():
                col_idx += 1
            number = int("".join(row[start:col_idx]))

            surroundings = []
            for pos in range(start, col_idx):
                surroundings.extend(get_surroundings(matrix, row_idx, pos))

            # Let's assume that there are no numbers with more than one '*' nearby
            gears = [position for (value, position) in surroundings if value == "*"]
            if len(gears) > 0:
                numbers_with_gears.append((number, gears[0]))
        else:
            col_idx += 1

gears = {}
for value, position in numbers_with_gears:
    if position not in gears:
        gears[position] = []
    gears[position].append(value)

# Gears with 2 part numbers
gears = [gears[g] for g in gears if len(gears[g]) == 2]

total = sum([x[0] * x[1] for x in gears])

print(total)

# 75741499
