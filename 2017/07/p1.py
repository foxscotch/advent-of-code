# Python 3.6.1

import re


def main():
    with open("input.txt", "r") as f:
        programs = {}
        for line in f:
            match = re.match(r"(\w+) \((\d+)\)(?: -> ([\w, ]+))?", line)
            if match is None:
                print("what")
            else:
                prog_name = match.group(1)
                weight = match.group(2)
                chstr = match.group(3)
                children = chstr.split(", ") if chstr else ()
                programs[prog_name] = (weight, children)

    all_children = []

    for program_info in programs.values():
        all_children += program_info[1]

    for program in programs.keys():
        if program not in all_children:
            print(program)
            break


if __name__ == "__main__":
    main()
