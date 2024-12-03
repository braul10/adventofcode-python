import re

with open("input.txt", "r") as f:
    text = f.read()

matches = []
next_dont = text[0:].index("don't()")
matches.extend(re.findall(r"mul\(\d+,\d+\)", text[:next_dont]))

idx = next_dont + 1
while idx < len(text):
    if text[idx] == "d" and text[idx:].startswith("do()"):
        try:
            next_dont = text[idx:].index("don't()")
            next_dont += idx
            matches.extend(re.findall(r"mul\(\d+,\d+\)", text[idx:next_dont]))
            idx = next_dont
        except:
            matches.extend(re.findall(r"mul\(\d+,\d+\)", text[idx:]))
    idx += 1

total = 0
for m in matches:
    m = m.replace("mul(", "").replace(")", "")
    first = m.split(",")[0]
    second = m.split(",")[1]
    total += int(first) * int(second)

print(total)

# 76729637