with open("05/input.txt") as file:
    rows = file.read().split("\n")

ranges = [list(map(int, r.split("-"))) for r in rows[: rows.index("")]]
ids = map(int, rows[rows.index("") + 1 :])
total = 0
for id in ids:
    for r in ranges:
        if id in range(r[0], r[1] + 1):
            total += 1
            break

print("Part 1:", total)

total = 0
ranges.sort(key=lambda r: r[0] - r[1])
for i, r in enumerate(ranges):
    for r2 in ranges[:i]:
        if r[0] >= r2[0] and r[0] <= r2[1]:
            r[0] = r2[1] + 1
        if r[1] >= r2[0] and r[1] <= r2[1]:
            r[1] = r2[0] - 1
    if r[1] >= r[0]:
        total += r[1] - r[0] + 1

print("Part 2:", total)
