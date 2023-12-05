import re
s = 'Аама мыла Ромо рама, папа ел горох'
def Vowels (string):
    a = re.findall(r'[а-яА-ЯёЁ]+', string)

    final = []
    for i in a:
        b = []
        b = re.findall(r'[уеыаоэёяиюУЕЫАОЭЁЯИЮ]', i)
        # map???? listcomplication - yeild???
        unique_elements = list(set(b))
        if len(unique_elements) == 1:
            final.append(i)

    final.sort(key = lambda x: (len(x), x.lower()))

    return final

print(Vowels(s))