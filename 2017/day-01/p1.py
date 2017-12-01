# Python 3.6.1 / Anaconda 4.4.0

with open('input.txt', 'r') as f:
    puz_in = [int(i) for i in f.read()[0:-1]]

puz_sum = 0
for pc in range(len(puz_in)):
    pn = pc + 1 if not pc == len(puz_in) - 1 else 0
    puz_cur = puz_in[pc]
    puz_next = puz_in[pn]

    if puz_cur == puz_next:
        puz_sum += puz_cur

print(puz_sum)
