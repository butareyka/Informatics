import re
s =  'ВТ 12ава    323 45324   (.;, ИТМО мама овыарвжоарп валфоы'

def VTITMO (string):
    a = re.findall(r'ВТ(?:\W+\w+|\W+){1,4}\s+ИТМО', string)
    b = []
    for i in a:
        b.append(re.sub(r'[^\w\s]+', '', i))

    return b

print(*VTITMO(s))
