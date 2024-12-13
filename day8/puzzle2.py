import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

antennas = {}
with open(filename, "r") as file:
    for i, line in enumerate(file):
        for j, c in enumerate(line):
            if c not in ".\n":
                antennas.setdefault(c, [])
                antennas[c].append(complex(i, j))
grid_width = j
grid_height = i + 1

antinodes = set()
for antenna, positions in antennas.items():
    for i, a1 in enumerate(positions):
        for a2 in positions[slice(i + 1, None)]:
            diff = a1 - a2
            antinode = a1
            while 0 <= antinode.real < grid_height and 0 <= antinode.imag < grid_width:
                antinodes.add(antinode)
                antinode += diff
            antinode = a2
            while 0 <= antinode.real < grid_height and 0 <= antinode.imag < grid_width:
                antinodes.add(antinode)
                antinode -= diff

print(f"Numbers of antinodes: {len(antinodes)}")
