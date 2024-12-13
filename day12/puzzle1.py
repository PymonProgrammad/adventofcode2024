import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

garden: dict[str, set[complex]] = {}
with open(filename, "r") as file:
    for i, line in enumerate(file):
        for j, plant in enumerate(line.strip()):
            garden.setdefault(plant, set())
            garden[plant].add(complex(i, j))

price: int = 0
for plant, positions in garden.items():
    while positions:
        first_pos = positions.pop()
        region: dict[complex, int] = {first_pos: 4}
        newly_added: list[complex] = [first_pos]
        while newly_added:
            for i in range(len(newly_added)):
                pos = newly_added.pop(0)
                for d in (1, -1, 1j, -1j):
                    neighbour = pos + d
                    if neighbour in positions:
                        positions.remove(neighbour)
                        region[neighbour] = 4
                        newly_added.append(neighbour)
                        for x in (1, -1, 1j, -1j):
                            if neighbour + x in region:
                                region[neighbour] -= 1
                                region[neighbour + x] -= 1
        price += sum(region.values()) * len(region)

print(f"Total price: {price}")
