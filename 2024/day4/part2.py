with open("input.txt") as f:
    lines = f.read().splitlines()

matrix = [list(line) for line in lines]


def get_in_direction(matrix, row, col, direction):
    rows, cols = len(matrix), len(matrix[0])
    dr, dc = direction
    nr, nc = row + dr, col + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        return matrix[nr][nc]
    else:
        return None


counter = 0
for row_idx, row in enumerate(matrix):
    col_idx = 0
    while col_idx < len(row):
        if row[col_idx] == "A":
            if (
                get_in_direction(matrix, row_idx, col_idx, (-1, -1)) == "M"
                and get_in_direction(matrix, row_idx, col_idx, (1, 1)) == "S"
                or get_in_direction(matrix, row_idx, col_idx, (-1, -1)) == "S"
                and get_in_direction(matrix, row_idx, col_idx, (1, 1)) == "M"
            ) and (
                get_in_direction(matrix, row_idx, col_idx, (1, -1)) == "M"
                and get_in_direction(matrix, row_idx, col_idx, (-1, 1)) == "S"
                or get_in_direction(matrix, row_idx, col_idx, (1, -1)) == "S"
                and get_in_direction(matrix, row_idx, col_idx, (-1, 1)) == "M"
            ):
                counter += 1

        col_idx += 1

print(counter)

# 1923
