# Python 3.6.1


def get_input():
    with open("input.txt", "r") as f:
        return f.read().strip().split(",")


def distance(x, y, z):
    return max(abs(x), abs(y), abs(z))


def main():
    steps = get_input()

    x, y, z = 0, 0, 0
    dist = 0
    max_dist = 0
    for step in steps:
        dist = distance(x, y, z)
        if dist > max_dist:
            max_dist = dist
        if step == "n":
            y += 1
            z -= 1
        elif step == "s":
            y -= 1
            z += 1
        elif step == "ne":
            x += 1
            z -= 1
        elif step == "sw":
            x -= 1
            z += 1
        elif step == "nw":
            y += 1
            x -= 1
        elif step == "se":
            y -= 1
            x += 1
        else:
            raise ValueError("Invalid direction.")

    print(max_dist)


if __name__ == "__main__":
    main()
