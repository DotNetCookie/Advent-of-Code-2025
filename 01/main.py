result_part_1 = 0
result_part_2 = 0
current_pos = 50

with open("./01/input.txt", "r") as file:
    for line in file:
        prev_pos = current_pos
        current_pos += int(line[1:]) * (-1 if line.startswith("L") else 1)
        result_part_2 += abs(int(current_pos / 100))
        result_part_2 += 1 if current_pos <= 0 and prev_pos != 0 else 0
        current_pos %= 100
        result_part_1 += 1 if current_pos == 0 else 0


print("Part 1: ", result_part_1)
print("Part 2: ", result_part_2)
