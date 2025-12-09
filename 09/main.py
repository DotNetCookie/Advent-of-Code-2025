from itertools import combinations
from shapely import Polygon

with open("09/input.txt") as file:
    coords = [tuple(map(int, r.split(","))) for r in file.read().split("\n")]

polygon = Polygon(coords)

max_area_1 = 0
max_area_2 = 0
for c1, c2 in combinations(coords, 2):
    area = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)
    max_area_1 = max(max_area_1, area)
    if polygon.contains(Polygon((c1, (c1[0], c2[1]), c2, (c2[0], c1[1])))):
        max_area_2 = max(max_area_2, area)

print("Part 1:", max_area_1)
print("Part 2:", max_area_2)
