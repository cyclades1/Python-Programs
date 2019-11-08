'''input
5
'''
def prime(n):
	for i in range(2,n-1):
		if n%i==0:
			print("NO")
			return
	print("YES")
	return
n = int(input())
prime(n)
