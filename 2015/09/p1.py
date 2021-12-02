with open("input.txt", "r") as file:
    input = file.read().split("\n")


class Traveler:
    def __init__(self):
        self._cities = {}
        self._paths = []

    @staticmethod
    def from_strings(l):
        for string in list:
            pass

    def get_city(self, city_name):
        return self._cities[city_name]


class City:
    def __init__(self, name, traveler):
        self.name = name
        self.traveler = traveler


class Path:
    def __init__(self, city1, city2, dist, traveler):
        self.city1 = city1
        self.city2 = city2
        self.dist = dist
        self.traveler = traveler

    @staticmethod
    def from_string(s, traveler):
        split = s.split(" ")

        start = split[0]
        end = split[2]
        dist = split[4]

        return Path(start, end, dist, traveler)
