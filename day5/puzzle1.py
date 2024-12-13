import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)


def list_index(lst: list, value, default=-1):
    return default if value not in lst else lst.index(value)


order = set()
with open(filename, "r") as file:
    while line := next(file).strip():
        order.add(tuple(line.split("|", maxsplit=2)[:2]))

    total = sum(
        int(update[len(update) // 2])
        for update in (line.strip().split(",") for line in file)
        if all(
            not any((x, y) in order for y in update[:i])
            and not any((y, x) in order for y in update[slice(i + 1, len(update))])
            for i, x in enumerate(update)
        )
    )

print(f"Sum of well ordered updates' middle page numbers: {total}")
