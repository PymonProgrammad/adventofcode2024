import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

topographic_map: list[list[int]] = []
trailheads: list[list[tuple[int, int]]] = []
with open(filename, "r") as file:
    for i, line in enumerate(file):
        line = line.strip()
        topographic_map.append([int(c) for c in line])
        trailheads.extend([(i, j)] for j, c in enumerate(line) if c == "0")

for trail_length in range(1, 10):
    for _i in range(len(trailheads)):
        trails = trailheads.pop(0)
        for _j in range(len(trails)):
            i, j = trails.pop(0)
            m, n = 0, 1
            for _k in range(4):
                if (
                    0 <= i + m < len(topographic_map)
                    and 0 <= j + n < len(topographic_map[0])
                    and topographic_map[i + m][j + n] == trail_length
                ):
                    trails.append((i + m, j + n))
                m, n = -n, m
        if trails:
            trailheads.append(trails)

total = sum(len(set(trails)) for trails in trailheads)

print(f"Total ratings: {total}")
