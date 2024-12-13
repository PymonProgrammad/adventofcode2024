import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

lab: str
with open(filename, "r") as file:
    lab = file.read()

grid_width: int = lab.find("\n") + 1
lab = ("\n" * grid_width) + lab
lab = lab + ("\n" * grid_width)
guard_pos: complex = complex(*divmod(lab.find("^"), grid_width))

obstacle_positions: set[complex] = set()
direction: complex = complex(-1)
while lab[int(guard_pos.real * grid_width + guard_pos.imag)] != "\n":
    for i in range(2):
        new_pos: complex = guard_pos + direction
        if lab[int(new_pos.real * grid_width + new_pos.imag)] == "#":
            direction = complex(direction.imag, -direction.real)
        else:
            break
    else:
        raise RuntimeError("A wall mysteriously appeared behind the guard!")

    # print(f"Looking for possible loop... {guard_pos} {direction}")
    loop_direction: complex = complex(direction.imag, -direction.real)
    loop_pos: complex = guard_pos + loop_direction
    loop: set[tuple[complex, complex]] = {(guard_pos, direction)}
    while (loop_pos, loop_direction) not in loop:
        loop.add((loop_pos, loop_direction))
        cell = lab[int(loop_pos.real * grid_width + loop_pos.imag)]
        if cell == "\n":
            break
        if cell == "#":
            loop_pos -= loop_direction
            loop_direction = complex(loop_direction.imag, -loop_direction.real)
        loop_pos += loop_direction
    else:
        obstacle_positions.add(new_pos)
    guard_pos = new_pos


print(f"Number of distinct possible new obstacle positions: {len(obstacle_positions)}")
