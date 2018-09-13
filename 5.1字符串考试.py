Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s='What is your name'
>>> s[11:2:-2]
'ro it'
>>> def is_pamax(name):
	low=0
	high=len(name)-1
	while low<high:
		if name[low]!=name[high]:
			return False
		low+=1
		high-=1
	return True

>>> f=open('G:/names.txt')
>>> max_length=0
>>> for line in f:
	name=line.strip()
	if is_pamax(name):
		temp_length=len(name)
		if temp_length>max_length:
			max_length=temp_length

			
>>> print(max_length)
8
>>> f.close()
>>> f=open('G:/names.txt')
>>> for line in f:
	name=line.strip()
	if is_pamax(name):
		if 8 ==len(name):
			print(name)

			
TREFFERT
>>> s='hello'
>>> y=0
>>> for i in s:
	y+=1
	print(y,i)

	
1 h
2 e
3 l
4 l
5 o
>>> s1='cbabc'
>>> index=0
>>> s2=''
>>> 
>>> while index<len(s1)-1:
	if s1[index]>s1[index+1]:
		s2+=s1[index]
	else:
		s2=s2*2
	index+=1

	
>>> print(s2)
cbcbcbcb
>>> 
