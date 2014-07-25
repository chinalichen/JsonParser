str = '{"a":12,"b":3,"cdasfewafdsafefdsaf":"dsafe"}'
index = 0
length = len(str)

def parse_json():
    parse_object()
    print "success"

def parse_object():
    global index, length, str
    while index < length:
        char = str[index+1]
        if char == '}':
            index+=1
            print "object end, pos:" , index
            return True
        elif char == '"':
            parse_attribute()
        elif ' ':
            index+=1
        elif ',':
            index+=1
        else:
            raise SyntaxError(index)

def parse_attribute():
    global index, length, str
    index+=1
    parse_string()
    if not str[index] == ':':
        raise SyntaxError(index)
    index+=1
    parse_value()

def parse_value():
    global index, length, str
    index+=1
    while True:
        if str[index] == ',':
            index-=1
            break;
        if str[index] == '}':
            index-=1
            break;
        index+=1

def parse_string():
    global index, length, str
    index+=1;
    while True:
        if str[index] == '"':
            index+=1
            break;
        index+=1

parse_json()