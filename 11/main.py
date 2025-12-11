with open("11/input.txt") as file:
    rows = file.read().split("\n")

flows = {r.split(": ")[0]: r.split(": ")[1].split(" ") for r in rows}


def get_path(key):
    outs = flows.get(key, [])
    total = 0
    for o in outs:
        if o == "out":
            total += 1
        else:
            total += get_path(o)
    return total


print("Part 1:", get_path("you"))
