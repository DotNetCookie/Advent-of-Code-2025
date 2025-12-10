from itertools import combinations

with open("10/input.txt") as file:
    rows = file.read().split("\n")


def sim_buttons(lights, buttons):
    for b in buttons:
        for x in b:
            lights[x] = not lights[x]
    return lights


total = 0
for row in rows:
    parts = row.split(" ")
    lights = [p == "#" for p in parts.pop(0).replace("[", "").replace("]", "")]
    joltage = map(int, parts.pop().replace("{", "").replace("}", "").split(","))
    buttons = [
        list(map(int, b.replace("(", "").replace(")", "").split(","))) for b in parts
    ]
    i = 1
    while True:
        for b in combinations(buttons, i):
            if True not in sim_buttons(list(lights), b):
                total += i
                break
        else:
            i += 1
            continue
        break


print("Part 1:", total)
