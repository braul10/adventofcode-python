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
            surroundings.append(matrix[nr][nc])
    return surroundings


valid_numbers = []

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

            if any(c not in "0123456789." for c in surroundings):
                valid_numbers.append(number)
        else:
            col_idx += 1

total = sum(valid_numbers)
print(total)
