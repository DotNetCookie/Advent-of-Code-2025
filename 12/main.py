with open("12/input.txt") as file:
    rows = file.read().split("\n")

shapes, shape = [], []
for row in rows[:30]:
    if row == "":
        shapes.append(len([y for x in shape for y in x if y == "#"]))
        shape = []
    elif ":" not in row:
        shape.append(row)

total = 0
for row in rows[30:]:
    dimensions, shapes_needed = row.split(": ")
    width, height = dimensions.split("x")
    area_needed = sum(
        [shapes[i] * c for i, c in enumerate(map(int, shapes_needed.split(" ")))]
    )
    if int(width) * int(height) - area_needed >= 0:
        total += 1

print(total)
