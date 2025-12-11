with open("11/input.txt") as file:
    rows = file.read().split("\n")

flows = {r.split(": ")[0]: r.split(": ")[1].split(" ") for r in rows}


def get_path_1(key):
    outs = flows.get(key, [])
    total = 0
    for o in outs:
        if o == "out":
            total += 1
        else:
            total += get_path_1(o)
    return total


cache = {}


def get_path_2(key, path=()):
    if key not in cache:
        outs = flows.get(key, [])
        total_out, total_solve = 0, 0
        fft, dac = 0, 0
        for o in outs:
            if o == "out":
                total_out += 1
            else:
                r = get_path_2(o, path + (key,))
                total_out += r[0]
                if key == "dac":
                    dac += r[0]
                    fft += r[1]
                    total_solve += r[1]
                elif key == "fft":
                    fft += r[0]
                    dac += r[2]
                    total_solve += r[2]
                else:
                    fft += r[1]
                    dac += r[2]
                    total_solve += r[3]
        cache[key] = (total_out, fft, dac, total_solve)
    return cache[key]


print("Part 1:", get_path_1("you"))
print("Part 2:", get_path_2("svr")[3])
