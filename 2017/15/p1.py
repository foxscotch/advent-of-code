# Python 3.6.1

divisor = 2147483647
last_16 = 0b1111111111111111


def generate(start, factor):
    return (start * factor) % divisor

def compare(gen_a, gen_b):
    return (gen_a & last_16) == (gen_b & last_16)

def main():
    gen_a = 703
    gen_b = 516
    a_factor = 16807
    b_factor = 48271

    counter = 0
    for _ in range(40_000_000):
        if compare(gen_a, gen_b):
            counter += 1
        gen_a = generate(gen_a, a_factor)
        gen_b = generate(gen_b, b_factor)

    print(counter)


if __name__ == '__main__':
    main()
