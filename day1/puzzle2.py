left, right = [], []
with open("input", "r") as file:
    for line in file.readlines(14000):
        pair = line.split(maxsplit=3)
        left.append(int(pair[0]))
        right.append(int(pair[1]))

print(
    "Similarity score:",
    sum(v * right.count(v) for v in left),
)
