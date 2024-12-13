def pairwise(iterable):
    STOP = object()
    it = iter(iterable)
    fst = next(it, STOP)
    if fst is STOP:
        return
    while (snd := next(it, STOP)) is not STOP:
        yield fst, snd
        fst = snd


def skip(iterable, index):
    it = iter(iterable)
    try:
        for i in range(index):
            yield next(it)
        next(it)
        while True:
            yield next(it)
    except StopIteration:
        pass


def is_safe_record(data: list[int]):
    return any(
        all(
            (
                lambda prev_sign: (
                    1 <= absd <= 3 and prev_sign in (prev_sign := d / absd, 0)
                    for d in (x - y for x, y in pairwise(skip(data, index)))
                    for absd in (abs(d),)
                )
            )(0)
        )
        for index in range(len(data))
    )


with open("input", "r") as file:
    count = len(
        [
            None
            for line in file
            if is_safe_record([int(x) for x in line.strip().split()])
        ]
    )

print(f"Number of safe records: {count}")
