import re

from math import prod


with open("06/input.txt") as file:
    rows = [re.split(r"\s+", row.strip()) for row in file.read().split("\n")]

total = 0
for c in [
    [int(e[i]) if e[i] not in "*+" else e[i] for e in rows] for i in range(len(rows[0]))
]:
    total += prod(c[:-1]) if c[-1] == "*" else sum(c[:-1])

print("Part 1:", total)


with open("06/input.txt") as file:
    rows = file.read().split("\n")

total = 0
nums = []
operator = ""
for i in range(len(rows[0]) + 1):
    num = "".join([row[i] for row in rows[:-1]]).strip() if i < len(rows[0]) else ""
    if num == "":
        total += prod(nums) if operator == "*" else sum(nums)
        nums.clear()
    else:
        if rows[-1][i] != " ":
            operator = rows[-1][i]
        nums.append(int(num))

print("Part 2:", total)
