import sys
import re

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

robots = (([], []), ([], []))
with open(filename, "r") as file:
    for line in file:
        m = re.match(
            r"p=(100|[1-9]?[0-9]),(10[0-2]|[1-9]?[0-9]) v=(-?\d+),(-?\d+)$", line
        )
        robot = complex(*map(int, m.group(1, 2))) + 100 * complex(
            *map(int, m.group(3, 4))
        )
        robot = complex(robot.real % 101, robot.imag % 103)
        if robot.real != 50 and robot.imag != 51:
            robots[int(robot.real) // 51][int(robot.imag) // 52].append(robot)

safety_factor = (
    len(robots[0][0]) * len(robots[0][1]) * len(robots[1][0]) * len(robots[1][1])
)

print(f"Safety factor: {safety_factor}")
