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


# Originally I took a class-based approach for houses as well, but the way I
# went about it seemed pretty slow, so I'm doing it differently now.

# House = {(x, y): presents}


santa = Santa()
houses = {(0, 0): 1}

for direction in puzzle_input:
    santa.move(direction)
    position = santa.get_pos()
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

# After running it, this method is clearly FAR faster.
# We're talking 9.8 seconds versus 0.2.
