import re

def is_Identifier(s):
    if re.match('[a-zA-Z_][a-zA-Z0-9_]*',s):
        return True
    else:
        return False


params=[]
while True:
    s=input('Please input:')
    if s=='':
        break
    else:
        params.append(s)

for s in params:
    if is_Identifier(s):
        print('True')
    else:
        print('False')
