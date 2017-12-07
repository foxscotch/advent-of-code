# Python 3.6.1

with open('input.txt', 'r') as f:
    banks = [int(i) for i in f.read()[:-1].split('\t')]

banks = [0, 2, 7, 0]
print(f'{banks} START')

seen = []  # List of encountered arrangements.
redis = 0  # Container for blocks to be redistributed.

i = 0
counter = 0
while True:
    if i >= len(banks):
        i = 0

    if redis == 0:
        if banks in seen:
            break
        else:
            seen.append(list(banks))

        redis_i = banks.index(max(banks))
        redis = banks[redis_i]
        banks[redis_i] = 0
        counter += 1

        print(banks)
    elif redis > 0:
        banks[i] += 1
        redis -= 1
        i += 1

print(f'{banks} STOP')
# print(counter)
