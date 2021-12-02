with open("input.txt", "r") as f:
    puzzle_input = f.read().replace("\n", "")

# Coordinates: (x, y)
class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        if direction == "^":
            self.y += 1
        elif direction == ">":
            self.x += 1
        elif direction == "<":
            self.x += -1
        elif direction == "v":
            self.y += -1

    def get_pos(self):
        return (self.x, self.y)


# House = {(x, y): presents}


santa = Santa()
robosanta = Santa()
houses = {(0, 0): 2}
turn = 0

for direction in puzzle_input:
    if turn == 0:
        santa.move(direction)
        position = santa.get_pos()
        turn = 1
    elif turn == 1:
        robosanta.move(direction)
        position = robosanta.get_pos()
        turn = 0
    if position in houses:
        houses[position] += 1
    else:
        houses[position] = 1


def total_with_presents():
    total = 0
    for num in houses.values():
        if num > 0:
            total += 1
    return total


print(total_with_presents())
