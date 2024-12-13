import sys
from typing import TextIO, Generator

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)


def is_possible(test_value: int, numbers: list[int]) -> bool:
    if len(numbers) <= 1:
        return test_value == numbers[0]

    return is_possible(test_value - numbers[-1], numbers[:-1]) or (
        numbers[-1] != 0
        and test_value % numbers[-1] == 0
        and is_possible(test_value // numbers[-1], numbers[:-1])
    )


def extract_data(file: TextIO) -> Generator[tuple[int, list[int]], None, None]:
    for line in file:
        value, numbers = line.split(":")
        yield int(value), [int(n) for n in numbers.split()]


with open(filename, "r") as file:
    values = list(
        test_value
        for test_value, numbers in extract_data(file)
        if is_possible(test_value, numbers)
    )
    total = sum(values)

print(f"Total calibration result: {total}")
