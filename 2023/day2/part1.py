with open("input.txt", "r") as f:
    lines = f.readlines()

game_idx = 1
possible_games = []
for line in lines:
    line = line.strip().split(": ")[1]
    sets = line.split("; ")
    possible = True
    for s in sets:
        colors = s.split(", ")

        green, red, blue = 0, 0, 0

        for color in colors:
            if "green" in color:
                green = int(color.split(" ")[0])
            if "red" in color:
                red = int(color.split(" ")[0])
            if "blue" in color:
                blue = int(color.split(" ")[0])

        if red > 12 or green > 13 or blue > 14:
            possible = False

        if not possible:
            break

    if possible:
        possible_games.append(game_idx)

    game_idx += 1

total = sum(possible_games)

print(total)

# 2006
