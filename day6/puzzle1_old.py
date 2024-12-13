import sys
import re

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    zone = file.read()

grid_width = zone.find("\n") + 1
guard_pos = divmod(zone.find("^"), grid_width)

guard_path = {guard_pos}
direction = "UP"
while True:
    guard_index = guard_pos[0] * grid_width + guard_pos[1]
    if direction == "UP":
        m = re.search(
            r"^.{"
            + str(grid_width - guard_pos[1] - 2)
            + r"}\#.{"
            + str(guard_pos[1])
            + r"}$",
            zone[slice(guard_pos[0] * grid_width + guard_pos[1], None, -1)],
            re.M,
        )
        if m is None:
            guard_path.update((i, guard_pos[1]) for i in range(guard_pos[0]))
            break
        end = guard_index - m.start() + 1
        obst_row = end // grid_width
        guard_path.update((i, guard_pos[1]) for i in range(obst_row + 1, guard_pos[0]))
        guard_pos = obst_row + 1, guard_pos[1]
        direction = "RIGHT"
    elif direction == "DOWN":
        m = re.search(
            r"^.{"
            + str(guard_pos[1])
            + r"}\#.{"
            + str(grid_width - guard_pos[1] - 2)
            + r"}$",
            zone[slice(guard_pos[0] * grid_width + guard_pos[1], None)],
            re.M,
        )
        if m is None:
            guard_path.update(
                (i, guard_pos[1])
                for i in range(guard_pos[0] + 1, len(zone) // grid_width)
            )
            break
        start = guard_index + m.start()
        obst_row = start // grid_width
        guard_path.update((i, guard_pos[1]) for i in range(guard_pos[0] + 1, obst_row))
        guard_pos = obst_row - 1, guard_pos[1]
        direction = "LEFT"
    elif direction == "LEFT":
        obst_col = (
            zone.rfind("#", guard_index - guard_pos[1], guard_index)
            - guard_index
            + guard_pos[1]
        )
        if obst_col == -1:
            guard_path.update((guard_pos[0], i) for i in range(guard_pos[1]))
            break
        guard_path.update((guard_pos[0], i) for i in range(obst_col + 1, guard_pos[1]))
        guard_pos = guard_pos[0], obst_col + 1
        direction = "UP"
    elif direction == "RIGHT":
        obst_col = (
            zone.find("#", guard_index, guard_index - guard_pos[1] + grid_width)
            - guard_index
            + guard_pos[1]
        )

        if obst_col == -1:
            guard_path.update(
                (guard_pos[0], i) for i in range(guard_pos[1] + 1, grid_width - 1)
            )
            break
        guard_path.update((guard_pos[0], i) for i in range(guard_pos[1] + 1, obst_col))
        guard_pos = guard_pos[0], obst_col - 1
        direction = "DOWN"

print(f"Number of distinct visited positions: {len(guard_path)}")
