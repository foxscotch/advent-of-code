import re


with open('input.txt', 'r') as file:
    input = file.read()[:-1]

example_string = '""\n"abc"\n"aaa\\"aaa"\n"\\x27"'             # 42, 23, 19
test_string = '"what\\\\when"\n"smash\\"hit"\n"rofl\\x04mao"'  # 54, 37, 17


def get_diff(s):
    lines = s.split('\n')
    code_len = 0
    enc_len = 0

    for line in lines:
        code_len += len(line)
        
        step = 0
        while step < len(line):
            if line[step] is '\\' or line[step] is '"':
               enc_len += 2
            else:
                enc_len += 1
            step += 1

        enc_len += 2

    return enc_len, code_len, enc_len - code_len


print(get_diff(example_string))
print(get_diff(test_string))
print(get_diff(input))
