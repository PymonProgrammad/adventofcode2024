import sys

filename = "input"

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    ws = [line.strip() for line in file]

TARGET = "XMAS"
REV_TARGET = TARGET[::-1]

count = len(
    [
        None
        for i in range(len(ws))
        for j in range(len(ws[i]))
        for word in (
            ws[i][slice(j, j + len(TARGET))],
            "".join(ws[i + k][j] for k in range(min(len(TARGET), len(ws) - i))),
            "".join(
                ws[i + k][j + k]
                for k in range(min(len(TARGET), len(ws) - i, len(ws[i]) - j))
            ),
            "".join(
                ws[i + k][j - k] for k in range(min(len(TARGET), len(ws) - i, j + 1))
            ),
        )
        if word in (TARGET, REV_TARGET)
    ]
)

print(f'Occurrences of "{TARGET}": {count}')
