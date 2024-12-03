with open("input.txt", "r") as f:
    lines = f.read().splitlines()

columns_base = 0
for idx, line in enumerate(lines):
    if line.startswith(" 1"):
        columns_base = idx
        break

number_of_columns = int([x for x in lines[columns_base].split(" ") if len(x) > 0][-1])

columns = [[] for x in range(number_of_columns)]
for line in lines[:columns_base]:
    idx = 0
    col_idx = 0
    while col_idx < len(columns):
        letter = line[idx : idx + 3].replace(" ", "").replace("[", "").replace("]", "")
        if len(letter) > 0:
            columns[col_idx].append(letter)
        idx += 4
        col_idx += 1

columns = [x[::-1] for x in columns]

for instruction in lines[columns_base + 2 :]:
    moves = int(instruction.split(" ")[1])
    c_from = int(instruction.split(" ")[3])
    c_to = int(instruction.split(" ")[5])

    for _ in range(moves):
        value = columns[c_from - 1].pop()
        columns[c_to - 1].append(value)

solution = "".join([x[-1] for x in columns])
print(solution)

# SHMSDGZVC
