import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    diskmap = [int(c) for c in file.readline().strip()]

if len(diskmap) % 2 == 0:
    diskmap.pop()

max_id = len(diskmap) // 2

index = -1
block_id = [1, max_id]
pos = diskmap.pop(0)
checksum = 0
while diskmap:
    n = min(diskmap[0], diskmap[-1])
    checksum += block_id[1] * sum(range(pos, pos + n))
    pos += n
    if n == diskmap[0]:
        diskmap[-1] -= n
        diskmap.pop(0)
        n = diskmap.pop(0)
        checksum += block_id[0] * sum(range(pos, pos + n))
        block_id[0] += 1
        pos += n
    else:
        diskmap[0] -= n
        diskmap.pop()
        diskmap.pop()
        block_id[1] -= 1


print(f"Checksum: {checksum}")
