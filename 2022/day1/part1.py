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

max_calories = max(elves_calories)

print(max_calories)

# 68802
