# Python 3.6.1 / Official

puzzle_input = 25 #265149

def same_sign(a, b):
    return abs(a + b) == abs(a) + abs(b)

x = 0
y = 0
cur_num = 1
cur_layer = 0
while cur_num != puzzle_input:
    to_print = []

    if y == -cur_layer and x == cur_layer:
        x += 1
        cur_layer += 1
        to_print.append('NEW_LAYER {:>2}'.format(cur_layer))
    elif abs(y) == cur_layer:
        if y > 0 and x > -cur_layer:
            x -= 1
        elif y < 0 and x < cur_layer:
            x += 1
        else:
            to_print.append('BROKE_ON_X_MOVE')
    elif abs(x) == cur_layer:
        pass
    else:
        to_print.append('BROKE_IN_GENERAL')

    cur_num += 1
    print('NUMBER {:>2}    POS ({:> 3}, {:> 3})    {}'.format(cur_num, x, y, '    '.join(to_print)))
