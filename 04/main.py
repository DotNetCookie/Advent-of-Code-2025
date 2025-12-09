with open("04/input.txt") as file:
    tiles = [list(row) for row in file.read().split("\n")]
    forklift_count = 0
    new_forklift_count = -1
    while new_forklift_count != 0:
        new_forklift_count = 0
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                if (
                    tile == "@"
                    and len(
                        [
                            1
                            for y2 in range(max(y - 1, 0), min(y + 2, len(tiles)))
                            for x2 in range(max(x - 1, 0), min(x + 2, len(tiles[y2])))
                            if tiles[y2][x2] in "@x"
                        ]
                    )
                    < 5
                ):
                    new_forklift_count += 1
                    tiles[y][x] = "x"

        if forklift_count == 0:
            print("Part 1:", new_forklift_count)

        forklift_count += new_forklift_count
        tiles = [[(tile if tile != "x" else ".") for tile in row] for row in tiles]

    print("Part 2:", forklift_count)
