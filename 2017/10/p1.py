# Python 3.6.1


class LoopingList(list):
    def __getitem__(self, key):
        if type(key) is int:
            return super().__getitem__(key % len(self))
        elif type(key) is slice:
            return [
                self[i]
                for i in range(default(key.start, 0), key.stop, default(key.step, 1))
            ]
        else:
            return super().__getitem__(key)

    def __setitem__(self, key, value):
        if type(key) is int and type(value) is list:
            for i in range(len(value)):
                self[key + i] = value[i]
        elif type(key) is int:
            super().__setitem__(key % len(self), value)
        else:
            super().__setitem__(key, value)


def default(val, d):
    return d if val is None else val


def reverse(numbers, pos, length):
    numbers[pos] = list(reversed(numbers[pos : pos + length]))


def main():
    numbers = LoopingList(range(256))
    lengths = [76, 1, 88, 148, 166, 217, 130, 0, 128, 254, 16, 2, 130, 71, 255, 229]

    # Example from challenge text:
    # numbers = LoopingList([0, 1, 2, 3, 4])
    # lengths = [3, 4, 1, 5]

    pos = 0
    skip = 0

    for length in lengths:
        reverse(numbers, pos, length)

        pos += skip + length
        skip += 1

    print(numbers[0] * numbers[1])


if __name__ == "__main__":
    main()
