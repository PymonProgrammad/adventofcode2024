class Iterator:
    def __init__(self):
        print("Iterator created")

    def __iter__(self):
        return self

    def __next__(self):
        print("Iterator pulled")
        raise StopIteration


class Iterable:
    def __init__(self):
        print("Iterable created")

    def __iter__(self):
        return Iterator()


def args_type(*args):
    print(type(args))


args_type(*Iterable())
