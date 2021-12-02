import re


# box_list will contain tuples in the format: (length, width, height)
box_list = []

regex = re.compile(r"^(\d+)x(\d+)x(\d+)$")

with open("input.txt", "r") as f:
    for line in f:
        match = regex.match(line)
        box_list.append((int(match.group(1)), int(match.group(2)), int(match.group(3))))

total_paper = 0

for box in box_list:
    sides = (box[0] * box[1], box[1] * box[2], box[2] * box[0]) * 2
    total_paper += sum(sides) + min(sides)

print(total_paper)
