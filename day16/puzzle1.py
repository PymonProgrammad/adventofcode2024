import sys
import math

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

start = None
end = None
vertice = {}
with open(filename, "r") as file:
    for i, line in enumerate(file):
        for j, c in enumerate(line.strip()):
            if c != "#":
                vertice.update(((i, j, k), [math.inf, None]) for k in range(4))
            if c == "S":
                start = (i, j, 0)
            elif c == "E":
                end = (i, j)
    width = j + 1
    height = i + 1

assert start and end, "Start or end not found"
vertice[start][0] = 0

edges = {
    (i, j, d): {
        (i, j, (d + 1) % 4): 1000,
        (i, j, (d + 3) % 4): 1000,
    }
    | {v: 1 for v in [(i + directions[d][0], j + directions[d][1], d)] if v in vertice}
    for i, j, d in vertice
}

q = list(vertice.keys())
while q:
    i, j, d = min(q, key=vertice.get)
    q.remove((i, j, d))
    for v, w in edges[i, j, d].items():
        if vertice[i, j, d][0] + w < vertice[v][0]:
            vertice[v][0] = vertice[i, j, d][0] + w
            vertice[v][1] = i, j, d

# v = min((end + (k,) for k in range(4)), key=vertice.get)
# path = []
# while v:
#     path.append(v)
#     v = vertice[v][1]
#
# for i in range(height):
#     for j in range(width):
#         for k in range(4):
#             if (i, j, k) in path:
#                 print(">^<v"[k], end="")
#                 break
#         else:
#             if (i, j, k) in vertice:
#                 print(".", end="")
#             else:
#                 print("#", end="")
#     print()

print(f"Minimum score to end: {min(vertice[end + (k,)][0] for k in range(4))}")
