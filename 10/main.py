from itertools import combinations

with open("10/input.txt") as file:
    rows = file.read().split("\n")


def sim_lights_buttons(lights, buttons):
    for b in buttons:
        for x in b:
            lights[x] = not lights[x]
    return lights


def get_hash(t):
    r = 0
    for i in t:
        r *= 1000
        r += i
    return r


total_1 = 0
total_2 = 0
for row in rows:
    parts = row.split(" ")
    lights = [p == "#" for p in parts.pop(0).replace("[", "").replace("]", "")]
    joltage = tuple(map(int, parts.pop().replace("{", "").replace("}", "").split(",")))
    buttons = [
        tuple(map(int, b.replace("(", "").replace(")", "").split(","))) for b in parts
    ]
    i = 1
    while True:
        for b in combinations(buttons, i):
            if True not in sim_lights_buttons(list(lights), b):
                total_1 += i
                break
        else:
            i += 1
            continue
        break

    joltage_hash = get_hash(joltage)
    length = len(joltage)
    empty_state = tuple(0 for _ in range(length))
    seen = {get_hash(empty_state): 0}
    minimal_i = None
    buttons = tuple(tuple(1 if i in b else 0 for i in range(length)) for b in buttons)
    states = {get_hash(empty_state): empty_state}
    while states:
        new_states = {}
        for state_key, state in states.items():
            i = seen[state_key] + 1
            if minimal_i is not None and i >= minimal_i:
                continue
            for button in buttons:
                result = []
                for s, b, j in zip(state, button, joltage):
                    r = s + b
                    if r > j:
                        break
                    result.append(r)
                else:
                    result = tuple(result)
                    result_hash = get_hash(result)
                    if result_hash == joltage_hash:
                        minimal_i = i
                        print(minimal_i)
                        seen[result_hash] = i
                    elif result_hash not in seen or i < seen[result_hash]:
                        seen[result_hash] = i
                        new_states[result_hash] = result
        states = new_states
    total_2 += minimal_i
    print(minimal_i, total_2, row)

print("Part 1:", total_1)
print("Part 2:", total_2)
