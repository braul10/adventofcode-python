with open("input.txt", "r") as f:
    lines = f.readlines()


def get_number(line):
    numbers = []
    for c in line:
        try:
            int(c)
            numbers.append(c)
        except:
            pass

    return f"{numbers[0]}{numbers[-1]}"


def transform_line(line):
    new_line = ""
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for idx in range(len(line)):
        if type(line[idx]) == int:
            new_line = new_line + line[idx]
        else:
            found = False
            for idx2, n in enumerate(list(numbers.keys()), 1):
                if line[idx:].startswith(n):
                    found = True
                    new_line = new_line + str(idx2)
                    break

            if not found:
                new_line = new_line + line[idx]

    return new_line


total = 0
for line in lines:
    transformed_line = transform_line(line)
    total += int(get_number(transformed_line))

print(total)

# 53389
