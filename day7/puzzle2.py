import sys
from typing import TextIO, Generator

sys.argv.pop(0)
filename = "input" if not sys.argv else sys.argv.pop(0)


def is_possible(test_value: int, numbers: list[str]) -> bool:
    if len(numbers) <= 1:
        return test_value == int(numbers[0])

    number = numbers[-1]
    inumber = int(number)
    others = numbers[:-1]
    svalue = str(test_value)
    return (
        is_possible(test_value - inumber, others)
        or (
            inumber != 0
            and test_value % inumber == 0
            and is_possible(test_value // inumber, others)
        )
        or (
            svalue.endswith(number)
            and is_possible(int(svalue.removesuffix(number)), others)
        )
    )


def extract_data(file: TextIO) -> Generator[tuple[int, list[str]], None, None]:
    for line in file:
        value, numbers = line.split(":")
        yield int(value), numbers.split()


with open(filename, "r") as file:
    total = sum(
        test_value
        for test_value, numbers in extract_data(file)
        if is_possible(test_value, numbers)
    )

print(f"Total calibration result: {total}")
