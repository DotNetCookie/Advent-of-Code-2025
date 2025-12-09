import math
from itertools import combinations
from typing import Dict, List, Self, Set, Tuple


class Box:
    def __init__(self, value: str):
        self.value = value
        [self.x, self.y, self.z] = map(int, value.split(","))

    def distance(self, other: Self):
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Box) and self.value == other.value


with open("08/input.txt") as file:
    boxes = [Box(row) for row in file.read().split("\n")]

distances: List[Tuple[int, Box, Box]] = []
for b1, b2 in combinations(boxes, 2):
    distances.append((b1.distance(b2), b1, b2))
distances.sort(key=lambda d: d[0])

circuits: List[Set[Box]] = []
circuit_of: Dict[Box, Set[Box]] = {}

i = 0
for dist, b1, b2 in distances:
    if i == 1000:
        print(
            "Part 1:",
            math.prod(sorted([len(c) for c in circuits], reverse=True)[:3]),
        )
    i += 1

    c1 = circuit_of.get(b1)
    c2 = circuit_of.get(b2)
    if c1 is not None and c1 is c2:
        continue

    if c1 is None and c2 is None:
        circuit = {b1, b2}
        circuits.append(circuit)
        circuit_of[b1] = circuit
        circuit_of[b2] = circuit
    elif c1 is not None and c2 is None:
        c1.add(b2)
        circuit_of[b2] = c1
    elif c2 is not None and c1 is None:
        c2.add(b1)
        circuit_of[b1] = c2
    else:
        if len(c1) < len(c2):
            c1, c2 = c2, c1
        for b in c2:
            c1.add(b)
            circuit_of[b] = c1
        circuits.remove(c2)

    if len(circuits) == 1 and len(circuits[0]) == len(boxes):
        print("Part 2:", b1.x * b2.x)
        break
