import re
l = []
while True:
    s = input()
    if s == '':
        break
    else:
        l.append(s)
        for s in l:
            if re.match('[a-zA-Z_]', s):
                if re.search('[_]|w', s):
                    print('True')
                else:
                    print('False')
