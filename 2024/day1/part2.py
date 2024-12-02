with open("input.txt", "r") as f:
    lines = f.readlines()

column1, column2 = [], []

for line in lines:
    column1.append(int(line.strip().split("   ")[0]))
    column2.append(int(line.strip().split("   ")[1]))

result = sum([i * column2.count(i) for i in column1])

print(result)

# 23082277
