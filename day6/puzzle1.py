import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    lab = file.read()

grid_width = lab.find("\n") + 1
guard_pos = divmod(lab.find("^"), grid_width)
guard_pos = complex(guard_pos[0], guard_pos[1])

guard_path = {guard_pos}
direction = -1
guard_index = int(guard_pos.real * grid_width + guard_pos.imag)
while 0 <= guard_index < len(lab) and lab[guard_index] != "\n":
    for i in range(4):
        new_pos = guard_pos + direction
        if (
            0
            <= (guard_index := int(new_pos.real * grid_width + new_pos.imag))
            < len(lab)
            and lab[guard_index] == "#"
        ):
            direction = complex(direction.imag, -direction.real)
        else:
            break
    else:
        raise RuntimeError("The guard has been mysteriously trapped!")
    guard_pos = new_pos
    guard_path.add(guard_pos)


print(f"Number of distinct positions in the guard's path: {len(guard_path)-1}")
