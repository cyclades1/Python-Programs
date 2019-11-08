'''input
12
'''
n = int(input())
d = 0
num = n 
while n>0:
	d*=10
	d += n%10
	n//=10
if(d==num):
	print("Yes")
else:
	print("No")

