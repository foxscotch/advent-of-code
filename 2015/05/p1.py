def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    total = 0
    for char in string:
        if char in vowels:
            total += 1
    return total


def contains_doubles(string):
    for i in range(len(string)):
        try:
            if string[i] == string[i + 1]:
                return True
        except IndexError:
            return False
    return False


def no_blacklisted(string):
    blacklist = ["ab", "cd", "pq", "xy"]
    for i in range(len(string)):
        try:
            if string[i] + string[i + 1] in blacklist:
                return False
        except IndexError:
            return True
    return False


# I made the other three functions first, then I decided it would be better if
# all the checks were part of a single loop, and therefore a single function.


def is_valid(string):
    contains_doubles = False
    no_blacklisted = True

    vowels = ["a", "e", "i", "o", "u"]
    total_vowels = 0

    blacklist = ["ab", "cd", "pq", "xy"]

    for i in range(len(string)):
        if string[i] in vowels:
            total_vowels += 1
        try:
            if not contains_doubles:
                if string[i] == string[i + 1]:
                    contains_doubles = True
            if no_blacklisted:
                if string[i] + string[i + 1] in blacklist:
                    no_blacklisted = False
        except IndexError:
            pass

    return total_vowels >= 3 and contains_doubles and no_blacklisted


with open("input.txt", "r") as f:
    total = 0
    for line in f:
        if is_valid(line):
            total += 1

print(total)
