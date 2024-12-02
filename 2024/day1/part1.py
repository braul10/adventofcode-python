with open("input.txt", "r") as f:
    lines = f.readlines()

column1, column2 = [], []

for line in lines:
    column1.append(int(line.strip().split("   ")[0]))
    column2.append(int(line.strip().split("   ")[1]))

column1.sort()
column2.sort()

result = sum([abs(column2[idx] - i) for idx, i in enumerate(column1)])

print(result)

# 2375403
