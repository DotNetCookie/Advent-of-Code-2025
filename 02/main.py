import math

# Part 1
with open("02/input.txt", "r") as file:
    id_ranges = file.read().split(",")

total = 0
for id_range in id_ranges:
    [start, end] = id_range.split("-")
    for i in range(
        int(start[: max(math.floor(len(start) / 2), 1)]),
        int(end[: math.ceil(len(end) / 2)]) + 1,
    ):
        invalid_id = int(str(i) * 2)
        if invalid_id < int(start):
            continue
        if invalid_id > int(end):
            break
        total += invalid_id

print("Part 1:", total)

# Part 2
total = 0
for id_range in id_ranges:
    [start, end] = id_range.split("-")
    for i in range(int(start), int(end) + 1):
        for j in range(len(str(i)) // 2, 0, -1):
            if str(i)[:j] * (len(str(i)) // j) == str(i):
                total += i
                break

print("Part 2:", total)
