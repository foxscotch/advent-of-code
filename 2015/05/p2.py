import re


def is_valid(string):
    match_pairs_regex = re.compile(r".*(\w\w).*\1.*")
    sep_pairs_regex = re.compile(r".*(\w)\w\1.*")

    contains_matching_pairs = False
    contains_separated_pairs = False

    if match_pairs_regex.match(string):
        contains_matching_pairs = True

    if sep_pairs_regex.match(string):
        contains_separated_pairs = True

    return contains_matching_pairs and contains_separated_pairs


with open("input.txt", "r") as f:
    total = 0
    for line in f:
        if is_valid(line):
            total += 1

print(total)
