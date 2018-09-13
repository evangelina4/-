def PigLatin():
    s=input("please enter the sentence:")
    list=s.lower().split(" ")
    for i in range(len(list)):
        if(list[i][:1] in 'aeiou'):
            list[i]=list[i]+'hay'
        elif(list[i][:2]=='qu'):
            list[i]=list[2:]+'quay'
        else:
            num=getIndex(list[i])
            list[i]=list[i][num:]+list[i][0:num]+'ay'
    return list


def getIndex(s):
    for i in range(len(s)):
        if ((s[i] in 'aeiou')or(i!=0 and s[i]=='y')):
            return i
    return len(s)


result=PigLatin()
for i in range(len(result)):
    print(result[i],)
