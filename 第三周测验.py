num=30

if num%2 == 0:
    print(num,'is even')
elif num %3 ==0:
    print(num,'is multiple of 3')




x=1
y=-1
z=1
if x > 0: 
    if y > 0:
        print ('AAA' )
elif z > 0:
    print( 'BBB')



y=0
for i in range(0,10,2):
    y+=i
print(y)



number = int(input('Enter an integer: '))
max = number
while number != 0:
    number = int(input('Enter an integer: '))
    if number > max:
        max = number
print(max)
