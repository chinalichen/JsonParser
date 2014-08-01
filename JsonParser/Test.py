#def parse_digit():
#    if str[index]>='0' and str[index]<='9':
#        index+=1
#        return true
#    return false

def parse_digits():
    global index, length, str
    start = index
    while str[index].isdigit():
        index+=1
    if start != index:
        return str[start:index]
    raise SyntaxError(index)

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
    return parse_digits()

def parse_frac():
    global index, length, str
    if str[index] == '.':
        index += 1
        return '.' + parse_digits()
    raise SyntaxError(index+1)

def parse_number():
    global index, length, str
    start = index
    parse_int()
    if str[index] == '.':
        parse_frac()
    return str[start:index]
    

str = "-0.0asdfasdf}"
index = 0
length = len(str)

print parse_number()