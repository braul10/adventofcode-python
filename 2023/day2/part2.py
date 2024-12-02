with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.strip().split(": ")[1]
    sets = line.split("; ")

    green, red, blue = [], [], []
    for s in sets:
        colors = s.split(", ")

        for color in colors:
            if "green" in color:
                green.append(int(color.split(" ")[0]))
            if "red" in color:
                red.append(int(color.split(" ")[0]))
            if "blue" in color:
                blue.append(int(color.split(" ")[0]))

    max_green, max_red, max_blue = max(green), max(red), max(blue)
    total += max_green * max_red * max_blue

print(total)

# 84911
