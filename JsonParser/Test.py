def parse_digits():


def parse_int():
    global index, length, str
    start = index
    char = str[index]
    if char == '0':
        if str[index+1].isdigit():
            raise SyntaxError(index+1)
        else:
            index += 1
            return 0
    if char == '-':
        index += 1
    elif char == '+':
        index += 1
    while str[index].isdigit():
        index += 1
    return str[start: index]

def parse_frac():
    global index, length, str
    if str[index] == '.':
        index += 1
        int = parse_int()
    return '.'+int
str = ".+123}"
index = 0
length = len(str)

print parse_frac()