# Python 3.6.1

puzzle_input = 265149

x = 0
y = 0
cur_num = 1
cur_layer = 0

while cur_num != puzzle_input:
    if y == -cur_layer and x == cur_layer:
        x += 1
        cur_layer += 1
    elif y == cur_layer and x > -cur_layer:
        x -= 1
    elif y == -cur_layer and x < cur_layer:
        x += 1
    elif x == cur_layer and y < cur_layer:
        y += 1
    elif x == -cur_layer and y > -cur_layer:
        y -= 1

    cur_num += 1

print("RESULT {}".format(abs(x) + abs(y)))
