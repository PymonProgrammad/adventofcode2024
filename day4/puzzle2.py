import sys

filename = "input"

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    ws = [line.strip() for line in file]

count = len(
    [
        None
        for i in range(1, len(ws) - 1)
        for j in range(1, len(ws[i]) - 1)
        if ws[i][j] == "A"
        and ws[i - 1][j - 1] + ws[i + 1][j + 1] in ("MS", "SM")
        and ws[i - 1][j + 1] + ws[i + 1][j - 1] in ("MS", "SM")
    ]
)

print(f"Occurrences of X-MAS: {count}")
