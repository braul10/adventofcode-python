with open("input.txt", "r") as f:
    lines = f.readlines()

lines = list(map(str.strip, lines))

# A/X: Rock
# B/Y: Paper
# C/Z: Scissors


def calculate_win(player, me):
    if (
        player == "A"
        and me == "X"
        or player == "B"
        and me == "Y"
        or player == "C"
        and me == "Z"
    ):
        return 3
    if player == "A" and me == "Y":
        return 6
    if player == "A" and me == "Z":
        return 0
    if player == "B" and me == "X":
        return 0
    if player == "B" and me == "Z":
        return 6
    if player == "C" and me == "X":
        return 6
    if player == "C" and me == "Y":
        return 0

def get_win(player):
    if player == 'A':
        return 'Y'
    if player == 'B':
        return 'Z'
    if player == 'C':
        return 'X'

def get_draw(player):
    if player == 'A':
        return 'X'
    if player == 'B':
        return 'Y'
    if player == 'C':
        return 'Z'
    
def get_lose(player):
    if player == 'A':
        return 'Z'
    if player == 'B':
        return 'X'
    if player == 'C':
        return 'Y'

score = 0
for line in lines:
    player = line.split(" ")[0]
    result = line.split(" ")[1]

    if result == 'X':
        me = get_lose(player)
    elif result == 'Y':
        me = get_draw(player)
    elif result == 'Z':
        me = get_win(player)

    round_points = 0
    if me == "X":
        round_points = 1
    elif me == "Y":
        round_points = 2
    elif me == "Z":
        round_points = 3

    round_points += calculate_win(player, me)
    score += round_points

print(score)

# 13221
