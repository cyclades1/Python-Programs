'''input
7
'''

def febo(n):
	if n ==0:
		return n
	if n ==1:
		return n
	else:
		return febo(n-1)+febo(n-2)

n = int(input())
print (febo(n))