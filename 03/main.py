with open("./03/input.txt") as file:
    rows = file.read().split("\n")

total = 0
for row in rows:
    values = list(map(int, row))
    values = values[values.index(max(values[:-1])) :]
    max_value = str(values.pop(0))
    max_value += str(values.pop(values.index(max(values))))
    total += int(max_value)

print("Part 1:", total)

total = 0
for row in rows:
    max_value = ""
    for i in range(12):
        index = row.index(max(row if i == 11 else row[: i - 11]))
        max_value += row[index]
        row = row[index + 1 :]
    total += int(max_value)

print("Part 2:", total)
