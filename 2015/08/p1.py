with open("input.txt", "r") as file:
    input = file.read().replace("\n", "")

example_string = r'"""abc""aaa\"aaa""\x27"'  # 23, 11, 12
test_string = r'"what\\when""smash\"hit""rofl\x04mao"'  # 37, 26, 11


# originally was using regex. this faster? maybe. never got the regex to work
# well enough for timing


def get_diff(s):
    code_len = len(s)

    step = 0
    mem_len = 0
    while step < len(s):
        if s[step] is "\\":
            if s[step + 1] is "x":
                mem_len += 1
                step += 4
            else:
                mem_len += 1
                step += 2
        elif s[step] is '"':
            step += 1
        else:
            mem_len += 1
            step += 1

    return code_len, mem_len, code_len - mem_len


print(get_diff(example_string))
print(get_diff(test_string))
print(get_diff(input))
