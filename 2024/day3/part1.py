import re

with open("input.txt", "r") as f:
    text = f.read()

matches = re.findall(r"mul\(\d+,\d+\)", text)

total = 0
for m in matches:
    m = m.replace("mul(", "").replace(")", "")
    first = m.split(",")[0]
    second = m.split(",")[1]
    total += int(first) * int(second)

print(total)

# 178794710
