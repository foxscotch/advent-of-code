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
    with open('input.txt', 'r') as f:
        banks = [int(i) for i in f.read()[:-1].split('\t')]

    seen = []  # List of encountered arrangements.
    looking_for = None  # Will be used for the bank we want to find again.

    i = 0
    counter = 0
    while True:
        if banks == looking_for:
            break

        if counter == 0 and banks in seen:
            counter += 1
            looking_for = list(banks)
        elif counter > 0:
            counter += 1
        
        seen.append(list(banks))
        distribute(banks, banks.index(max(banks)))
        

    print(counter)

if __name__ == '__main__':
    main()
