import sys
import re

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

machines: list[list[tuple[int, int]]] = []
with open(filename, "r") as file:
    machine = []
    for line in file:
        if m := re.match(r"Button A: X\+(\d+), Y\+(\d+)$", line):
            machine.append(tuple(int(x) for x in m.groups("0")))
        elif m := re.match(r"Button B: X\+(\d+), Y\+(\d+)$", line):
            machine.append(tuple(int(x) for x in m.groups("0")))
        elif m := re.match(r"Prize: X=(\d+), Y=(\d+)$", line):
            machine.append(tuple(int(x) + 10000000000000 for x in m.groups("0")))
        elif line == "\n":
            machines.append(machine)
            machine = []
    if machine:
        machines.append(machine)

tokens = 0
for machine in machines:
    a = divmod(
        machine[1][1] * machine[2][0] - machine[1][0] * machine[2][1],
        machine[1][1] * machine[0][0] - machine[1][0] * machine[0][1],
    )
    b = divmod(machine[2][1] - machine[0][1] * a[0], machine[1][1])
    if a[1] == 0 and b[1] == 0:
        tokens += 3 * a[0] + b[0]

print(f"Tokens needed: {tokens}")
