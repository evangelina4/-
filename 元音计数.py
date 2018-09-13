def vowel_count(s):
    count=0
    for i in s:
        if i in 'aeiouAEIOU':
            count+=1
    return count

str='I love sandwich'
print(vowel_count(str))
