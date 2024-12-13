left, right = [], []
with open("input", "r") as file:
    for line in file.readlines(14000):
        pair = line.split(maxsplit=3)
        left.append(int(pair[0]))
        right.append(int(pair[1]))

print(
    "Total distance:",
    sum(map(lambda t: abs(t[0] - t[1]), zip(sorted(left), sorted(right)))),
)
