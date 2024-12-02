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


total = 0
for line in lines:
    total += int(get_number(line))

print(total)

# 54338
