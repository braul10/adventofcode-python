with open("input.txt") as f:
    lines = f.read().splitlines()

matrix = [list(line) for line in lines]


def get_in_direction(matrix, row, col, direction):
    rows, cols = len(matrix), len(matrix[0])
    dr, dc = direction
    nr, nc = row + dr, col + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        return matrix[nr][nc], nr, nc
    else:
        return None, None, None


counter = 0
for row_idx, row in enumerate(matrix):
    col_idx = 0
    while col_idx < len(row):
        if row[col_idx] == "X":
            for direction in [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]:
                value, r, c = get_in_direction(matrix, row_idx, col_idx, direction)
                if value == "M":
                    value, r, c = get_in_direction(matrix, r, c, direction)
                    if value == "A":
                        value, r, c = get_in_direction(matrix, r, c, direction)
                        if value == "S":
                            counter += 1

        col_idx += 1

print(counter)

# 2504
