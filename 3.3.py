sum=0
extra=0
for num in range(1,10):
    if num%2 and not num%3:
        sum+=num
    else:
        extra+=1

print(extra)
