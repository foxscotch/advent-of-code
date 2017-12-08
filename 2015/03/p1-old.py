with open('input.txt', 'r') as f:
    puzzle_input = f.read().replace('\n', '')

# Coordinates: (x, y)
class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == '>':
            self.x += 1
        elif direction == '<':
            self.x += -1
        elif direction == 'v':
            self.y += -1

    def get_pos(self):
        return (self.x, self.y)


class House:
    houses = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.presents = 0

        House.houses.append(self)

    def deliver(self):
        self.presents += 1

    def get_pos(self):
        return (self.x, self.y)

    @classmethod
    def get_house(cls, house_coords):
        for house in cls.houses:
            if house_coords == (house.x, house.y):
                return house
        return None

    @classmethod
    def total_houses(cls):
        return len(cls.houses)

    @classmethod
    def total_presents(cls):
        total = 0
        for house in cls.houses:
            total += house.presents
        return total

    @classmethod
    def total_with_presents(cls):
        current_total = 0
        for house in cls.houses:
            if house.presents > 0:
                current_total += 1
        return current_total


santa = Santa()

House.get_house((0, 0)).deliver()

for direction in puzzle_input:
    santa.move(direction)
    house = House.get_house(santa.get_pos())
    if house is not None:
        house.deliver()
    else:
        House(*santa.get_pos())

print(House.total_houses())
print(House.total_presents())
print(House.total_with_presents())
