import re

with open("input", "r") as file:
    data = file.read()

total = sum(
    int(x) * int(y)
    for x, y in re.findall(r"mul\(([1-9][0-9]{,2}),([1-9][0-9]{,2})\)", data)
)

print(f"Sum of mul operations: {total}")
