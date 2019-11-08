'''input
1010
'''
s = str(input())
n = 0
for i in s:
	n*=2
	n+=int(i)
print(n)
