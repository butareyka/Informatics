import re
string = 'X-OsdlfjXPXD:OX-OX-oX-O'

def smile(string):
    a = re.findall('X-O', string)
    return len(a)

print(smile(string))
