def getStrValue (letter):  
    alph = "abcdefghijklmnopqrstuvwxyz"  
    letter = letter.lower()  
    return alph.find(letter) + 1  
   
params = []  
while True:  
    s = input()  
    if s == '':  
        break  
    else:  
        params.append(s)  
   
for word in params:  
    sum = 0  
    for letter in word:  
        sum += getStrValue(letter)  
   
    print(sum)  
