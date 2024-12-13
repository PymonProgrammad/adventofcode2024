with open("input", "r") as file:
    count = 0
    for line in file:
        data = [int(x) for x in line.strip().split()]
        diffs = [x - y for x, y in zip(data, data[1:])]
        if all(1 <= abs(d) <= 3 for d in diffs) and abs(
            sum(x / abs(x) for x in diffs)
        ) == len(diffs):
            count += 1

print(f"Number of safe records: {count}")
