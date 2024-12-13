import sys
from math import log10

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    stones = [int(n) for n in file.readline().split()]

this_step = {s: stones.count(s) for s in stones}
next_step = {}

for i in range(75):
    for stone, count in this_step.items():
        if stone == 0:
            next_step.setdefault(1, 0)
            next_step[1] += count
        else:
            q, r = divmod(int(log10(stone)) + 1, 2)
            if r == 0:
                for n in divmod(stone, 10**q):
                    next_step.setdefault(n, 0)
                    next_step[n] += count
            else:
                n = stone * 2024
                next_step.setdefault(n, 0)
                next_step[n] += count
    this_step = next_step
    next_step = {}

total = sum(x for x in this_step.values())

print(f"Number of stones: {total}")
