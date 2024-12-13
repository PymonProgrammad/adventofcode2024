import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    diskmap = [
        (i // 2 * (i % 2), int(c))
        for i, c in enumerate(file.readline().strip(), start=1)
    ]


if len(diskmap) % 2 == 0:
    diskmap.pop()

pos = diskmap.pop(0)[1]

i = len(diskmap) - 1
while i > 0:
    for j in range(i):
        if diskmap[j][0] > 0 or diskmap[i][1] > diskmap[j][1]:
            continue
        diskmap[j] = diskmap[j][0], diskmap[j][1] - diskmap[i][1]
        diskmap.insert(j, diskmap[i])
        diskmap[i + 1] = 0, diskmap[i + 1][1]
        break
    else:
        i -= 1
    while diskmap[i][0] == 0:
        i -= 1

checksum = 0
for id, n in diskmap:
    checksum += id * sum(range(pos, pos + n))
    pos += n

print(f"Checksum: {checksum}")
