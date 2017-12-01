# Python 3.6.1 / Anaconda 4.4.0

with open('input.txt', 'r') as f:
    puz_in = [int(i) for i in f.read()[0:-1]]

puz_sum = 0
puz_inc = len(puz_in) // 2
for pc in range(len(puz_in)):
    puz_cur = puz_in[pc]
    puz_next = puz_in[(pc + puz_inc) % len(puz_in)]

    if puz_cur == puz_next:
        puz_sum += puz_cur

print(puz_sum)
