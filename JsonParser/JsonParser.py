str = '''{"type":"gcSolidColorBrush","color":{"a":255,"r":0,"g":0,"b":0}}'''
index = 0
length = len(str)

def parse_json():
    skip_whitespace()
    parse_object()
    skip_whitespace()
    if index != length:
        raise SyntaxError(index)
    print "success"

def parse_object():
    global index, length, str
    index += 1
    skip_whitespace()
    if str[index] == '}':
        index += 1
        print "object end, pos:" , index
        return {}
    while index < length:
        parse_attribute()
        skip_whitespace()
        if str[index] == ',':
            index+=1
            skip_whitespace()
            continue
        elif str[index] == '}':
            index += 1
            print "object end, pos:", index
            return {}
        else:
            raise SyntaxError(index)

def parse_attribute():
    global index, length, str
    parse_string()
    skip_whitespace()
    if not str[index] == ':':
        raise SyntaxError(index)
    index+=1
    skip_whitespace()
    parse_value()

def parse_value():
    global index, length, str
    start = index
    while True:
        char = str[index]
        if char == 't':
            value = parse_true()
        elif char == 'f':
            value = parse_false()
        elif char == 'n':
            value = parse_null()
        elif char == '"':
            value = parse_string()
        elif char == '{':
            value = parse_object()
        elif char == '[':
            value = parse_array()
        elif char.isdigit() or char=='-' or char == '+':
            value = parse_number()
        else:
            break
    if start == index:
        raise SyntaxError(index)
    return value

def parse_null():
    global index, length, str
    null = "null"
    pos = 0
    while pos < 4:
        if str[index] != null[pos]:
            raise SyntaxError(index)
        pos += 1
        index += 1
    return True

def parse_true():
    global index, length, str
    true = "true"
    pos = 0
    while pos < 5:
        if str[index] != true[pos]:
            raise SyntaxError(index)
        pos += 1
        index += 1
    return True

def parse_false():
    global index, length, str
    false = "false"
    pos = 0
    while pos < 5:
        if str[index] != false[pos]:
            raise SyntaxError(index)
        pos += 1
        index += 1
    return True
#[value,value,...]
def parse_array():
    global index, length, str
    index += 1
    while True:
        skip_whitespace()
        parse_value()
        skip_whiteSpace()
        if str[index] == ',':
            continue
        elif str[index] == ']':
            index+=1
            print "array end. pos:", index
            return True
        else:
            raise SyntaxError(index)

def parse_string():
    global index, length, str
    index+=1;
    while True:
        if str[index] == '"':
            index+=1
            break;
        index+=1

def parse_number():
    global index, length, str
    start = index
    if str[index] == '0':
        if str[index+1].isdigit():
            raise SyntaxError(index+1)
        else:
            index += 1
            return 0
    else:
        while str[index].isdigit():
            index+=1
    return str[start: index]

def parse_int():
    global index, length, str
    start = index
    if str[index] == '0':
        if str[index+1].isdigit():
            raise SyntaxError(index+1)
        else:
            index += 1
            return 0
    else:
        while str[index].isdigit():
            index+=1
    return str[start: index]

def skip_whitespace():
    global index, length, str
    while index < length:
        if str[index].isspace():
            index+=1
        else:
            break

parse_json()