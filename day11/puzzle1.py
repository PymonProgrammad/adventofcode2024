import sys

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)

with open(filename, "r") as file:
    stones = [int(n) for n in file.readline().split()]

for i in range(25):
    stones = [
        x
        for ls in (
            [1]
            if n == 0
            else (
                [n * 2024]
                if len(str(n)) % 2 == 1
                else list(divmod(n, 10 ** (len(str(n)) // 2)))
            )
            for n in stones
        )
        for x in ls
    ]

print(f"Number of stones: {len(stones)}")
