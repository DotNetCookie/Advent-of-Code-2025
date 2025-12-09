with open("07/input.txt") as file:
    rows = [list(r) for r in file.read().split("\n")]
    splits = 0
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if rows[y - 1][x] in "S|":
                if cell == "^":
                    splits += 1
                    row[x - 1] = "|"
                    row[x + 1] = "|"
                else:
                    row[x] = "|"
    print("Part 1:", splits)


with open("07/input.txt") as file:
    rows = [list(r) for r in file.read().split("\n")]

cache = {}


def get_timelines(y, x):
    cache.setdefault(y, {})
    if x not in cache[y]:
        if y > len(rows) - 1:
            result = 1
        elif rows[y][x] == "^":
            result = get_timelines(y + 1, x - 1) + get_timelines(y + 1, x + 1)
        else:
            result = get_timelines(y + 1, x)
        cache[y][x] = result
    return cache[y][x]


print("Part 2:", get_timelines(1, rows[0].index("S")))
