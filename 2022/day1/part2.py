with open("input.txt", "r") as f:
    lines = f.readlines()

elves_calories = []
elf_calories = 0
for line in lines:
    line = line.strip()
    if len(line) > 0:
        elf_calories += int(line)
    else:
        elves_calories.append(elf_calories)
        elf_calories = 0

elves_calories.sort()
total = sum(elves_calories[-3:])

print(total)

# 205370
