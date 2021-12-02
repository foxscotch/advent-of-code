# Python 3.6.1


class LoopingList(list):
    def chunks(self):
        chunks = []
        for i in range(16):
            chunks.append(self[i * 16 : i * 16 + 1])
        return chunks

    def xor_chunks(self):
        return [xor(*l) for l in self.chunks()]

    def hex_chunks(self):
        return bytes(self.xor_chunks()).hex()

    def reverse(self, pos, length):
        self[pos] = list(reversed(self[pos : pos + length]))

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


def xor(*args):
    res = args[0]
    for arg in args[1:]:
        res = res ^ arg
    return res


def main():
    numbers = LoopingList(range(256))
    lengths = b"76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"
    lengths += bytes([17, 31, 73, 47, 23])  # Standard suffix

    pos = 0
    skip = 0

    for _ in range(1):
        pos = pos % len(numbers)
        for length in lengths:
            numbers.reverse(pos, length)

            pos += skip + length
            skip += 1

    print(f"pos  {pos}\n" f"skip {skip}\n" f"hash {numbers.hex_chunks()}")


if __name__ == "__main__":
    main()
