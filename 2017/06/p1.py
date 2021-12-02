# Python 3.6.1


def distribute(banks, pos):
    blocks = banks[pos]
    banks[pos] = 0
    i = pos + 1
    while blocks > 0:
        banks[i % len(banks)] += 1
        blocks -= 1
        i += 1


def main():
    with open("input.txt", "r") as f:
        banks = [int(i) for i in f.read()[:-1].split("\t")]

    seen = []  # List of encountered arrangements.

    i = 0
    counter = 0
    while True:
        if banks in seen:
            break

        seen.append(list(banks))
        distribute(banks, banks.index(max(banks)))
        counter += 1

    print(counter)


if __name__ == "__main__":
    main()
