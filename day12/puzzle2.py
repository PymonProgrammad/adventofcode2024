import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

garden: dict[str, set[complex]] = {}
with open(filename, "r") as file:
    for i, line in enumerate(file):
        for j, plant in enumerate(line.strip()):
            garden.setdefault(plant, set())
            garden[plant].add(complex(i, j))

total_price = 0
for plant, positions in garden.items():
    while positions:
        first_pos = positions.pop()
        region: dict[complex, tuple[list[complex], list[complex]]] = {
            first_pos: ([], [])
        }
        newly_added: list[complex] = [first_pos]
        while newly_added:
            for i in range(len(newly_added)):
                pos = newly_added.pop(0)
                for d in (1, -1, 1j, -1j):
                    neighbour = pos + d
                    if neighbour in positions:
                        positions.remove(neighbour)
                        region[neighbour] = ([], [])
                        newly_added.append(neighbour)
                        for x in (1, -1, 1j, -1j):
                            if neighbour + x in region:
                                region[neighbour][0].append(x)
                                region[neighbour + x][0].append(-x)
                        for x in (1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j):
                            if neighbour + x in region:
                                region[neighbour][1].append(x)
                                region[neighbour + x][1].append(-x)
        price = sum(
            (
                4
                if not v[0]
                else 2
                if len(v[0]) == 1
                else 1
                if len(v[0]) == 2 and (v[0][0] + v[0][1])
                else 0
            )
            + len(
                [
                    None
                    for i, x in enumerate(v[0])
                    for y in v[0][slice(i + 1)]
                    if (x * y).real == 0 and x + y not in v[1]
                ]
            )
            for v in region.values()
        ) * len(region)
        total_price += price

print(f"Total price: {total_price}")
