import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    towels = file.readline().strip().split(", ")
    file.readline()
    patterns = [line.strip() for line in file]
towels = set(towels)

total = 0
for pat in patterns:
    subs = []
    lengths = {0: 1}
    start = 0
    while start < len(pat):
        length = lengths[start]
        while start + length <= len(pat):
            stop = start + length
            while stop <= len(pat):
                print(f"\r{stop:0>2} {pat[:stop]}", end="")
                print(" " * (len(pat) - stop), end=" ")
                print(*lengths.values(), sep="", end="")
                print(" " * (len(pat) - len(lengths)), end="")

                if pat[start:stop] in towels:
                    break
                stop += 1
            else:
                length += 1
                continue
            break
        else:
            lengths.pop(start)
            if not lengths:
                break
            start = max(lengths.keys())
            subs.pop()
            lengths[start] += 1
            continue
        subs.append(pat[start:stop])
        lengths[start] = stop - start
        start = stop
        lengths[start] = 1
    else:
        total += 1
    print()
    print(pat, subs)

print(f"Number of possible patterns: {total}")
