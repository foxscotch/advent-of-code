# Python 3.8.3

import re


class Rule:
    PATTERN = re.compile(r"(\d+): (\d+|\"[ab]\")( \d+)?(?: \| (\d+)( \d+)?)?")
    RULES = {}

    def __init__(self, string):
        match = self.PATTERN.match(string)

        self.id = int(match.group(1))
        self.RULES[self.id] = self

        if match.group(2).isnumeric():
            self.letter = None
            self.subrule1 = int(match.group(2) or -1), int(match.group(3) or -1)
            self.subrule2 = int(match.group(4) or -1), int(match.group(5) or -1)
        else:
            self.letter = match.group(2).strip('"')
            self.subrule1 = None
            self.subrule2 = None

    def construct_pattern(self):
        if self.letter:
            return self.letter

        sub1_cur, sub1_next = self.subrule1
        sub2_cur, sub2_next = self.subrule2

        left = self.RULES[sub1_cur].construct_pattern()
        if sub1_next >= 0:
            left += self.RULES[sub1_next].construct_pattern()

        right = ""
        if sub2_cur >= 0:
            right += self.RULES[sub2_cur].construct_pattern()
        if sub2_next >= 0:
            right += self.RULES[sub2_next].construct_pattern()

        return f"({left}|{right})" if right else left

    def __repr__(self):
        if self.letter:
            return "Rule(\"{}: '{}'\")".format(self.id, self.letter)
        return 'Rule("{}: {} {} | {} {}")'.format(
            self.id,
            self.subrule1[0],
            self.subrule1[1],
            self.subrule2[0],
            self.subrule2[1],
        )


def get_input():
    with open("input.txt", "r") as f:
        rules, messages = f.read().split("\n\n")
        yield [Rule(s) for s in rules.splitlines()]
        yield messages.splitlines()


def main():
    rules, messages = get_input()
    pattern = re.compile(Rule.RULES[0].construct_pattern())

    total = 0
    for message in messages:
        if pattern.fullmatch(message):
            total += 1
    return total


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
