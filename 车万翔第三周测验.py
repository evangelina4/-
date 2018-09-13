num=int(input('Enter the number:'))
sum=0


for i in range(3,num):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)




