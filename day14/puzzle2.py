import sys
import os
import re
import math


def mainloop(
    robots: list[tuple[complex, complex]],
    width: int,
    height: int,
    start: int,
    jump: int,
):
    BRAILLE_BITS = (
        (1, 3),
        (0, 3),
        (1, 2),
        (1, 1),
        (1, 0),
        (0, 2),
        (0, 1),
        (0, 0),
    )
    try:
        seconds = start
        while True:
            occupied_tiles = set(x[0] for x in robots)
            print(
                *(
                    "".join(
                        chr(
                            0x2800
                            + int(
                                "".join(
                                    "1"
                                    if complex(i * 2 + x, j * 4 + y) in occupied_tiles
                                    else "0"
                                    for x, y in BRAILLE_BITS
                                ),
                                base=2,
                            )
                        )
                        for i in range(math.ceil(width / 2))
                    )
                    for j in range(math.ceil(height / 4))
                ),
                sep="\n",
            )

            print(seconds)

            if "!" == input("Press Enter to continue or type ! to go back a step:"):
                step = -jump
            else:
                step = jump

            for robot in robots:
                robot[0] += step * robot[1]
                robot[0] = complex(robot[0].real % width, robot[0].imag % height)
            seconds += step
    except KeyboardInterrupt:
        print()
        sys.exit(0)


HELP = """Arguments: [file] [options]

Displays the state of the room each second and the number of seconds passed. Hit <Ctrl-C> to stop.
File defaults to "input"

Options:
  -w <value>               (width) Use <value> as width of the room (default: 101)
  -h <value>               (height) Use <value> as height of the room (default: 103)
  -s <value>               (start) Start on second number <value> (default: 0)
  -j <value>               (jump) Display every <value> second (default: 1)
  --help                   Display this help"""


if __name__ == "__main__":
    filename = None
    width = 101
    height = 103
    start = 0
    jump = 1

    sys.argv.pop(0)

    i: int = 1
    while sys.argv:
        arg = sys.argv.pop(0)
        if arg == "-w" and sys.argv:
            width = int(sys.argv.pop(0))
        elif arg == "-h" and sys.argv:
            height = int(sys.argv.pop(0))
        elif arg == "-s" and sys.argv:
            start = int(sys.argv.pop(0))
        elif arg == "-j" and sys.argv:
            jump = int(sys.argv.pop(0))
        elif arg == "--help":
            print(HELP)
            sys.exit(0)
        elif i == 1:
            filename = arg
        i += 1
    if filename is None:
        filename = "input"
    elif not os.path.isfile(filename):
        raise RuntimeError(f'file "{filename}" doesn\'t exist')

    robots = []
    with open(filename, "r") as file:
        for line in file:
            m = re.match(
                r"p=(100|[1-9]?[0-9]),(10[0-2]|[1-9]?[0-9]) v=(-?\d+),(-?\d+)$", line
            )
            robots.append(
                [complex(*map(int, m.group(1, 2))), complex(*map(int, m.group(3, 4)))]
            )
            robots[-1][0] += start * robots[-1][1]
            robots[-1][0] = complex(
                robots[-1][0].real % width, robots[-1][0].imag % height
            )

    mainloop(robots, width, height, start, jump)
